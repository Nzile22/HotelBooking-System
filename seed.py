from database import session
from models.Hotel import Hotel
from models.Booking import Booking

# Sample data for hotels
hotels = [
    {"name": "Hotel California", "location": "Los Angeles"},
    {"name": "The Grand Budapest Hotel", "location": "Budapest"},
    {"name": "The Ritz", "location": "Paris"},
]

# Sample data for bookings
bookings = [
    {"guest_name": "John Doe", "hotel_id": 1},
    {"guest_name": "Jane Smith", "hotel_id": 2},
    {"guest_name": "Alice Johnson", "hotel_id": 1},
]

def seed_data():
    # Seed hotels
    for hotel in hotels:
        Hotel.create(session, hotel["name"], hotel["location"])
    
    # Seed bookings
    for booking in bookings:
        Booking.create(session, booking["guest_name"], booking["hotel_id"])

if __name__ == "__main__":
    seed_data()
