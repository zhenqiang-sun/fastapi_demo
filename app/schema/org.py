from datetime import datetime

from fastapi_plus.schema.base import InfoSchema


class OrgInfoSchema(InfoSchema):
    category_id: int
    category_name: str
    parent_name: str


class OrgDetailSchema(OrgInfoSchema):
    created_time: datetime
    updated_time: datetime
