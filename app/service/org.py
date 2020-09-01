from fastapi_plus.service.base import BaseService

from ..dao.org import OrgDao
from ..model.org import Org


class OrgService(BaseService):
    def __init__(self, auth_data: dict = {}):
        user_id = auth_data.get('user_id', 0)
        self.Model = Org
        self.dao = OrgDao(user_id)
        self.dao.Model = Org

        super().__init__(user_id, auth_data)
