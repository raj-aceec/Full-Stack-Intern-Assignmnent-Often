from app.models import Itinerary
from app.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
db = SessionLocal()

def seed_itineraries():
    db.query(Itinerary).delete()
    itineraries = [
        Itinerary(title="Phuket Explorer - 3 Nights", duration_nights=3, region="Phuket"),
        Itinerary(title="Krabi Adventure - 4 Nights", duration_nights=4, region="Krabi"),
        Itinerary(title="Thailand Duo - Phuket & Krabi - 6 Nights", duration_nights=6, region="Phuket, Krabi"),
        Itinerary(title="Phuket Getaway - 2 Nights", duration_nights=2, region="Phuket"),
        Itinerary(title="Krabi Relaxation - 7 Nights", duration_nights=7, region="Krabi"),
        Itinerary(title="Island Hopping - 8 Nights", duration_nights=8, region="Phuket, Krabi")
    ]
    db.add_all(itineraries)
    db.commit()

seed_itineraries()
