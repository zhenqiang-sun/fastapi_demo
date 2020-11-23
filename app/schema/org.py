from datetime import datetime

from fastapi_plus.schema.base import InfoSchema, RespDetailSchema


class OrgInfoSchema(InfoSchema):
    category_id: int
    category_name: str
    parent_name: str


class OrgDetailSchema(OrgInfoSchema):
    created_time: datetime
    updated_time: datetime


class OrgRespDetailSchema(RespDetailSchema):
    detail: OrgDetailSchema = None
