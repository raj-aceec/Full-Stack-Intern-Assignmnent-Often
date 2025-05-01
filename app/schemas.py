from pydantic import BaseModel
from typing import List

class ItineraryCreate(BaseModel):
    title: str
    duration_nights: int
    region: str

class ItineraryOut(BaseModel):
    id: int
    title: str
    duration_nights: int
    region: str

    class Config:
        orm_mode = True
