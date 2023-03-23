from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
# from ..services import util, users

router = APIRouter()


@router.post("/create")
def create_addresses_entry():
    ...


@router.get("/read")
def get_all_addresses():
    ...


@router.get("/read/")
def get_address_by_id():
    ...


@router.put("/update/id")
def update_address_by_id():
    ...


@router.delete("/delete/id")
def delete_address_by_id():
    ...
