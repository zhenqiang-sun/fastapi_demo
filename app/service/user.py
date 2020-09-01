import hashlib
import uuid

from fastapi_plus.service.base import BaseService
from fastapi_plus.utils.obj2dict import obj2dict
from fastapi_plus.utils.redis import RedisUtils

from ..dao.user import UserDao
from ..model.user import User


class UserService(BaseService):
    def __init__(self, auth_data: dict = {}):
        user_id = auth_data.get('user_id', 0)
        self.Model = User
        self.dao = UserDao(user_id)
        self.dao.Model = User
        self.redis = RedisUtils()
        # self.wxapp = WxappUtils()

        super().__init__(user_id, auth_data)

    def login_by_code(self, code: str):
        """
        通过微信登录code进行登录
        :param code:
        :return:
        """

        # data = self.wxapp.jscode2session(code)
        #
        # if 'openid' not in data:
        #     return {
        #         'code': 500,
        #         'message': '错误：jscode2session'
        #     }
        #
        # return self.login_by_openid(data['openid'])
        pass

    def login_by_token(self, token: str):
        """
        通过自产token进行登录
        :param token:
        :return:
        """

        data = self.redis.get('token:' + token)

        if not data:
            return {
                'code': 500,
                'message': '错误：token错误'
            }

        # 删除当前token，因为会重新创建
        self.redis.delete('token:' + token)

        return self._login_by_id(data['user']['id'])

    def login_by_openid(self, openid: str):
        """
        通过openid进行登录
        :param openid:
        :return:
        """
        # user = self.dao.read_by_openid(openid)
        user = None

        if not user:
            user = User()
            user.openid = openid
            self.dao.create(user)

        return self._login_success(user)

    def _login_success(self, user):
        token = str(user.id) + str(uuid.uuid1())

        data = {
            'token': token,
            'user_id': user.id,
            'user': obj2dict(user),
        }

        self.redis.set('token:' + token, data, 360000)

        return data

    def _login_by_id(self, id: int):
        """
        通过id进行登录
        :param openid:
        :return:
        """

        user = self.dao.read(id)

        if not user:
            return {
                'code': 2008061621,
                'message': '用户不存在'
            }

        return self._login_success(user)

    def login_by_password(self, username: str, password: str):
        """
        通过username、password进行登录
        :param username:
        :param password:
        :return:
        """

        user = self.dao.read_by_username(username)

        if not user:
            return {
                'code': 2008061621,
                'message': '用户不存在'
            }

        if user.password != hashlib.md5((user.name + password).encode(encoding='UTF-8')).hexdigest():
            return {
                'code': 2008061622,
                'message': '密码错误'
            }

        return self._login_success(user)
