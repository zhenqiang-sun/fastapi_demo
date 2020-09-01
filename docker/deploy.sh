#!/bin/bash

# 停掉并清除旧的容器
docker-compose down

# 创建新的容器并后台启动
docker-compose up -d