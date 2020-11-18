from fastapi import APIRouter, Depends
from fastapi_plus.schema.base import ListArgsSchema, RespListSchema, RespBaseSchema, RespIdSchema
from fastapi_plus.utils.auth import get_auth_data
from fastapi_plus.utils.custom_route import CustomRoute

from ..schema.category import CategoryInfoSchema, CategoryRespDetailSchema
from ..service.category import CategoryService

router = APIRouter(route_class=CustomRoute)


@router.post('/list', response_model=RespListSchema)
async def list(*, args: ListArgsSchema, auth_data: dict = Depends(get_auth_data)):
    """
    读取类别数据列表
    :param args: 请求参数集
    :return: 类别列表结构
    """
    args.user_id = auth_data.get('user_id')
    return CategoryService(auth_data).list(args)


@router.get('/{id}', response_model=CategoryRespDetailSchema)
async def read(id: int, auth_data: dict = Depends(get_auth_data)):
    """
    读取类别数据详情
    :param id: 类别id 
    :return: 类别详情结构
    """
    resp = CategoryRespDetailSchema()
    resp.detail = CategoryService(auth_data).read(id)
    return resp


@router.post('', response_model=RespIdSchema, response_model_exclude_none=True)
async def create(*, info: CategoryInfoSchema, auth_data: dict = Depends(get_auth_data)):
    """
    创建类别数据
    :param info: 类别数据
    :return: 
    """
    return CategoryService(auth_data).create(info)


@router.put('/{id}', response_model=RespBaseSchema)
async def update(*, info: CategoryInfoSchema, auth_data: dict = Depends(get_auth_data)):
    """
    修改类别数据
    :param info: 类别数据
    :return:
    """
    return CategoryService(auth_data).update(info)


@router.delete('/{id}', response_model=RespBaseSchema)
async def delete(id: int, auth_data: dict = Depends(get_auth_data)):
    """
    删除类别数据
    :param id: 类别id
    :return:
    """
    return CategoryService(auth_data).delete(id)
