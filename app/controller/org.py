from typing import List

from fastapi import APIRouter, Depends
from fastapi_plus.schema.base import ListArgsSchema, ListSchema, ResponseSchema
from fastapi_plus.utils.auth import get_auth_data
from fastapi_plus.utils.custom_route import CustomRoute

from ..schema.org import OrgInfoSchema, OrgDetailSchema
from ..service.org import OrgService

router = APIRouter(route_class=CustomRoute)


@router.post('/select', response_model=List[ListSchema])
async def select(*, args: ListArgsSchema, auth_data: dict = Depends(get_auth_data)):
    args.user_id = auth_data.get('user_id')
    return OrgService(auth_data).list(args)


@router.post('/list', response_model=List[ListSchema])
async def list(*, args: ListArgsSchema, auth_data: dict = Depends(get_auth_data)):
    args.user_id = auth_data.get('user_id')
    return OrgService(auth_data).list(args)


@router.get('/{id}', response_model=OrgDetailSchema)
async def read(id: int, auth_data: dict = Depends(get_auth_data)):
    return OrgService(auth_data).read(id)


@router.post('', response_model=ResponseSchema, response_model_exclude_none=True)
async def create(*, info: OrgInfoSchema, auth_data: dict = Depends(get_auth_data)):
    return OrgService(auth_data).create(info)


@router.put('/{id}', response_model=ResponseSchema, response_model_exclude_none=True)
async def update(*, info: OrgInfoSchema, auth_data: dict = Depends(get_auth_data)):
    return OrgService(auth_data).update(info)


@router.delete("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete(id: int, auth_data: dict = Depends(get_auth_data)):
    return OrgService(auth_data).delete(id)
