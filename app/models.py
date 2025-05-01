from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Itinerary(Base):
    __tablename__ = 'itineraries'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration_nights = Column(Integer, nullable=False)
    region = Column(String, nullable=False)

    days = relationship("Day", back_populates="itinerary")

class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key=True)
    day_number = Column(Integer, nullable=False)
    itinerary_id = Column(Integer, ForeignKey('itineraries.id'))

    hotel = relationship("Hotel", back_populates="day", uselist=False)
    transfer = relationship("Transfer", back_populates="day", uselist=False)
    activities = relationship("Activity", back_populates="day")

    itinerary = relationship("Itinerary", back_populates="days")

class Hotel(Base):
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    day_id = Column(Integer, ForeignKey('days.id'))

    day = relationship("Day", back_populates="hotel")

class Transfer(Base):
    __tablename__ = 'transfers'
    id = Column(Integer, primary_key=True)
    from_location = Column(String)
    to_location = Column(String)
    mode = Column(String)
    time = Column(String)
    day_id = Column(Integer, ForeignKey('days.id'))

    day = relationship("Day", back_populates="transfer")

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    time = Column(String)
    day_id = Column(Integer, ForeignKey('days.id'))

    day = relationship("Day", back_populates="activities")
