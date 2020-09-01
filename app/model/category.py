from fastapi_plus.model.base import *


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'comment': '分类'}

    user_id = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='用户ID')
    parent_name = Column(String(255), nullable=False, server_default=text("''"), comment='父名称')
    parent_id_list = Column(String(500), nullable=False, server_default=text("''"), comment='父ID列表')
    parent_name_list = Column(String(1000), nullable=False, server_default=text("''"), comment='父名称列表')
    relation_obj = Column(String(255), nullable=False, server_default=text("''"), comment='相关对象')
