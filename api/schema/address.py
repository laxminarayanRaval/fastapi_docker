from pydantic import BaseModel


class AddressBase(BaseModel):
    latitude: float
    longitude: float


class AddressCreate(AddressBase):
    ...

class AddressGet(AddressBase):
    id : int

    class Config:
        orm_mode = True