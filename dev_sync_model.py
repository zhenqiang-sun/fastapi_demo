from fastapi_plus.utils.sync_model import SyncModel

from app.config.db import db_config

# 同步Model：根据数据库中的表结构。

if __name__ == '__main__':
    SyncModel().sync(db_config, is_use_base_model=True)
