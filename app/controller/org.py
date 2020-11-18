from fastapi import APIRouter, Depends
from fastapi_plus.schema.base import ListArgsSchema, RespListSchema, RespIdSchema, RespBaseSchema
from fastapi_plus.utils.auth import get_auth_data
from fastapi_plus.utils.custom_route import CustomRoute

from ..schema.org import OrgInfoSchema, OrgRespDetailSchema
from ..service.org import OrgService

router = APIRouter(route_class=CustomRoute)


@router.post('/list', response_model=RespListSchema)
async def list(*, args: ListArgsSchema, auth_data: dict = Depends(get_auth_data)):
    """
    读取组织数据列表
    :param args: 请求参数集
    :return: 组织列表结构
    """
    args.user_id = auth_data.get('user_id')
    return OrgService(auth_data).list(args)


@router.get('/{id}', response_model=OrgRespDetailSchema)
async def read(id: int, auth_data: dict = Depends(get_auth_data)):
    """
    读取组织数据详情
    :param id: 组织id
    :return: 组织详情结构
    """
    resp = OrgRespDetailSchema()
    resp.detail = OrgService(auth_data).read(id)
    return resp


@router.post('', response_model=RespIdSchema, response_model_exclude_none=True)
async def create(*, info: OrgInfoSchema, auth_data: dict = Depends(get_auth_data)):
    """
    创建组织数据
    :param info: 组织数据
    :return:
    """
    return OrgService(auth_data).create(info)


@router.put('/{id}', response_model=RespBaseSchema)
async def update(*, info: OrgInfoSchema, auth_data: dict = Depends(get_auth_data)):
    """
    修改组织数据
    :param info: 组织数据
    :return:
    """
    return OrgService(auth_data).update(info)


@router.delete("/{id}", response_model=RespBaseSchema)
async def delete(id: int, auth_data: dict = Depends(get_auth_data)):
    """
    删除组织数据
    :param id: 组织id
    :return:
    """
    return OrgService(auth_data).delete(id)
