
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.Booking import Booking

class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # Hotel name must be unique and cannot be null
    location = Column(String, nullable=False)

    bookings = relationship('Booking', back_populates='hotel', cascade="all, delete")

    def __repr__(self):
        return f"<Hotel(name={self.name}, location={self.location})>"

    @classmethod
    def create(cls, session, name, location):
        hotel = cls(name=name, location=location)
        session.add(hotel)
        session.commit()
        return hotel

    @classmethod
    def delete(cls, session, hotel_id):
        hotel = session.query(cls).filter_by(id=hotel_id).first()
        if hotel:
            session.delete(hotel)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, hotel_id):
        return session.query(cls).filter_by(id=hotel_id).first()
