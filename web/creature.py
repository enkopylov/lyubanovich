from typing import List

from fastapi import APIRouter, HTTPException

import data.creature as service
from errors import Missing, Duplicate
from model.creature import Creature

router = APIRouter(tags=['Creature'], prefix='/creature')


@router.get('')
@router.get('/')
def get_all() -> List[Creature]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> Creature | None:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


# пока не работают
@router.post('/')
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as exc:
        raise HTTPException(status_code=400, detail=exc.msg)


@router.patch('/')
def modify(creature: Creature) -> Creature:
    try:
        return service.modify(creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


# @router.put('/')
# def replace(creature: Creature) -> Creature:
#     return service.replace(creature)


@router.delete('/{name}')
def delete(name):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
