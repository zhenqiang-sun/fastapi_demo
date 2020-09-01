#!/bin/bash

# 安装：必须组件，使用阿里云源
pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /app/requirements.txt

# 进入应用目录
cd /app

# 使用uvicorn运行fastapi
uvicorn app.main:app --host 0.0.0.0 --port 8000
