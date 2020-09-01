from fastapi_plus.service.base import BaseService

from ..dao.category import CategoryDao
from ..model.category import Category


class CategoryService(BaseService):
    def __init__(self, auth_data: dict = {}):
        user_id = auth_data.get('user_id', 0)
        self.Model = Category
        self.dao = CategoryDao(user_id)
        self.dao.Model = Category

        super().__init__(user_id, auth_data)
