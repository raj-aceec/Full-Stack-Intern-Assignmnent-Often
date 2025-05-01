from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Itinerary
from app.schemas import ItineraryCreate, ItineraryOut
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Travel Itinerary API")

@app.post("/itineraries/", response_model=ItineraryOut)
def create_itinerary(itinerary: ItineraryCreate):
    db: Session = SessionLocal()
    db_itinerary = Itinerary(**itinerary.dict())
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary

@app.get("/itineraries/", response_model=List[ItineraryOut])
def get_itineraries():
    db: Session = SessionLocal()
    return db.query(Itinerary).all()
