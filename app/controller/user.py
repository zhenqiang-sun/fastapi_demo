from fastapi import APIRouter
from fastapi_plus.utils.custom_route import CustomRoute

from ..schema.auth import AuthDataSchema, LoginInputSchema
from ..service.user import UserService

router = APIRouter(route_class=CustomRoute)


@router.post('/login', response_model=AuthDataSchema, response_model_exclude_unset=True)
async def login(*, login_input: LoginInputSchema):
    if login_input.type == 'token':
        return UserService().login_by_token(login_input.key)
    elif login_input.type == 'openid':
        return UserService().login_by_openid(login_input.key)
    elif login_input.type == 'code':
        return UserService().login_by_code(login_input.key)
    elif login_input.type == 'password':
        return UserService().login_by_password(login_input.key, login_input.password)
    else:
        return {
            'code': 500,
            'message': '登录错误',
        }
