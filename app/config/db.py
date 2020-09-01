# 配置文件：DbConfig
from fastapi_plus.utils.db import DbConfig

db_config = DbConfig()
db_config.host = 'mariadb'
db_config.port = '3306'
db_config.username = 'root'
db_config.password = '1q2w3e4R'
db_config.database = 'fastapi_demo'
db_config.echo = True
