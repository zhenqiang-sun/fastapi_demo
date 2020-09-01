from typing import List

from fastapi import APIRouter, Depends
from fastapi_plus.schema.base import ListArgsSchema, ListSchema, ResponseSchema
from fastapi_plus.utils.auth import get_auth_data
from fastapi_plus.utils.custom_route import CustomRoute

from ..schema.category import CategoryDetailSchema, CategoryInfoSchema
from ..service.category import CategoryService

router = APIRouter(route_class=CustomRoute)


@router.post('/select', response_model=List[ListSchema])
async def select(*, args: ListArgsSchema, auth_data: dict = Depends(get_auth_data)):
    args.user_id = auth_data.get('user_id')
    return CategoryService(auth_data).list(args)


@router.post('/list', response_model=List[ListSchema])
async def list(*, args: ListArgsSchema, auth_data: dict = Depends(get_auth_data)):
    args.user_id = auth_data.get('user_id')
    return CategoryService(auth_data).list(args)


@router.get('/{id}', response_model=CategoryDetailSchema)
async def read(id: int, auth_data: dict = Depends(get_auth_data)):
    return CategoryService(auth_data).read(id)


@router.post('', response_model=ResponseSchema, response_model_exclude_none=True)
async def create(*, info: CategoryInfoSchema, auth_data: dict = Depends(get_auth_data)):
    return CategoryService(auth_data).create(info)


@router.put('/{id}', response_model=ResponseSchema, response_model_exclude_none=True)
async def update(*, info: CategoryInfoSchema, auth_data: dict = Depends(get_auth_data)):
    return CategoryService(auth_data).update(info)


@router.delete('/{id}', response_model=ResponseSchema, response_model_exclude_none=True)
async def delete(id: int, auth_data: dict = Depends(get_auth_data)):
    return CategoryService(auth_data).delete(id)
