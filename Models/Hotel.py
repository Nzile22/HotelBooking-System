# Importing the  necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.booking import Booking

class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)    # Hotel name, must be unique and cannot be null
    location = Column(String, nullable=False)

    bookings = relationship('Booking', back_populates='hotel', cascade="all, delete")

    def __repr__(self):
        return f"<Hotel(name={self.name}, location={self.location})>"
