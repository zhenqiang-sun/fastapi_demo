from fastapi_plus.schema.base import UserBaseSchema
from pydantic import BaseModel


class AuthDataSchema(BaseModel):
    code: int = 0
    message: str = 'SUCCESS'
    token: str = None
    user_id: int = None
    user: UserBaseSchema = None


class LoginInputSchema(BaseModel):
    type: str
    key: str
    password: str = None
