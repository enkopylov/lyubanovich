from typing import List

from fastapi import APIRouter, HTTPException

import data.explorer as service
from errors import Missing, Duplicate
from model.explorer import Explorer

router = APIRouter(prefix='/explorer')


@router.get('')
@router.get('/')
def get_all() -> List[Explorer]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> Explorer:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


# пока не работают
@router.post('/')
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=400, detail=exc.msg)


@router.patch('/')
def modify(explorer: Explorer) -> Explorer:
    try:
        return service.modify(explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


# @router.put('/')
# def replace(explorer: Explorer) -> Explorer:
#     return service.replace(explorer)


@router.delete('/{name}')
def delete(name):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
