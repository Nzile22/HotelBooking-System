from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    guest_name = Column(String, nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))

    hotel = relationship('Hotel', back_populates='bookings')

    def __repr__(self):
        return f"<Booking(guest={self.guest_name}, hotel_id={self.hotel_id})>"
