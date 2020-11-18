from fastapi_plus.model.base import Base
from sqlalchemy import create_engine

from app.config.db import db_config
from app.model import *

# 根据Mode创建DB数据表

if __name__ == '__main__':
    # 创建db连接
    engine = create_engine(db_config.get_url(), echo=True)

    # 创建db表
    Base.metadata.create_all(engine)
