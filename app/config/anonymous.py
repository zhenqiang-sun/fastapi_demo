from fastapi_plus.config import anonymous

# 匿名访问接口列表
anonymous_path_list = anonymous.anonymous_path_list + [
    '/v1/user/login',
]
