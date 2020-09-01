from fastapi_plus.model.base import *


class Org(Base):
    __tablename__ = 'org'
    __table_args__ = {'comment': '组织'}

    user_id = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='用户ID')
    category_id = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='分类ID')
    category_name = Column(String(255), nullable=False, server_default=text("''"), comment='分类名称')
    parent_name = Column(String(255), nullable=False, server_default=text("''"), comment='父名称')
