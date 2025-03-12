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

    @classmethod
    def create(cls, session, guest_name, hotel_id):
        booking = cls(guest_name=guest_name, hotel_id=hotel_id)
        session.add(booking)
        session.commit()
        return booking

    @classmethod
    def delete(cls, session, booking_id):
        booking = session.query(cls).filter_by(id=booking_id).first()
        if booking:
            session.delete(booking)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, booking_id):
        return session.query(cls).filter_by(id=booking_id).first()
