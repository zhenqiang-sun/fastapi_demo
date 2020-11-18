from fastapi_plus.utils.sync_model import SyncModel

from app.config.db import db_config

# 根据DB中的表结构修改Model。

if __name__ == '__main__':
    SyncModel().sync(db_config, is_use_base_model=True)
