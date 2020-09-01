from fastapi_plus.model.base import *


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'comment': '用户'}

    username = Column(String(255), nullable=False, server_default=text("''"), comment='账号')
    password = Column(String(255), nullable=False, server_default=text("''"), comment='密码')
