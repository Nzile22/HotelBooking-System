from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models.base import Base
from models.hotel import Hotel
from models.booking import Booking


# SQLite database setup
DATABASE_URL = "sqlite:///hotel_bookings.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = session()

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)


def create_tables():
    Base.metadata.create_all(engine)

# ORM Methods
def create_hotel(name, location):
    hotel = Hotel(name=name, location=location)
    session.add(hotel)
    session.commit()
    return hotel

def create_booking(guest_name, hotel_id):
    booking = Booking(guest_name=guest_name, hotel_id=hotel_id)
    session.add(booking)
    session.commit()
    return booking

def get_all_hotels():
    return session.query(Hotel).all()

def get_all_bookings():
    return session.query(Booking).all()

def find_hotel_by_id(hotel_id):
    return session.query(Hotel).filter_by(id=hotel_id).first()

def delete_hotel(hotel_id):
    hotel = find_hotel_by_id(hotel_id)
    if hotel:
        session.delete(hotel)
        session.commit()
        return True
    return False

def delete_booking(booking_id):
    booking = session.query(Booking).filter_by(id=booking_id).first()
    if booking:
        session.delete(booking)
        session.commit()
        return True
    return False
