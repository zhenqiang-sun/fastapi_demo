from datetime import datetime

from fastapi_plus.schema.base import InfoSchema


class CategoryInfoSchema(InfoSchema):
    parent_name: str
    relation_obj: str


class CategoryDetailSchema(CategoryInfoSchema):
    created_time: datetime
    updated_time: datetime
