from fastapi_plus.model.base import *


class EventLog(Base):
    __tablename__ = 'event_log'
    __table_args__ = {'comment': '事件记录'}

    user_id = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='用户ID')
    relation_obj = Column(String(255), nullable=False, server_default=text("''"), comment='相关对象')
    relation_id = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='相关ID')
    relation_name = Column(String(255), nullable=False, server_default=text("''"), comment='相关名称')
    event_id = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='事件id')
    event_time = Column(TIMESTAMP, comment='事件发生时间')
    event_from = Column(String(255), nullable=False, server_default=text("''"), comment='事件发生来源')
    before_data = Column(LONGTEXT, comment='之前数据')
    change_data = Column(LONGTEXT, comment='变化数据')
    after_data = Column(LONGTEXT, comment='之后数据')
