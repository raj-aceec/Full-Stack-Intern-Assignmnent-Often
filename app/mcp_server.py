from fastapi import FastAPI, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Itinerary
from typing import List

mcp_app = FastAPI(title="MCP Recommendation Server")

@mcp_app.get("/recommendations/", response_model=List[str])
def get_recommendations(nights: int = Query(..., ge=2, le=8)):
    db: Session = SessionLocal()
    results = db.query(Itinerary).filter(Itinerary.duration_nights == nights).all()
    if not results:
        return [f"No recommendations found for {nights} nights"]
    return [r.title for r in results]
