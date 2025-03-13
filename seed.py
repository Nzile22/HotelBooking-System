from faker import Faker
from models import Hotel, Booking
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import random

my_engine = create_engine("sqlite:///hotel_bookings.db")
session_inst = sessionmaker(bind=my_engine)
my_session = session_inst()

fake = Faker()

print("Start Seeding Hotels")
hotel_list = []
for i in range(10):
    new_hotel = Hotel(name=fake.name(), location=fake.address())
    hotel_list.append(new_hotel)
try:
    my_session.add_all(hotel_list)
    my_session.commit()
    print("Hotel seeded successfully")
    
    print("Start Seeding Bookings")
    booking_list = []
    for i in range(10):
        new_booking = Booking(guest_name=fake.name(), hotel_id=random.randint(1, 10))
        booking_list.append(new_booking)
    my_session.add_all(booking_list)
    my_session.commit()
    print("Bookings seeded successfully")
except Exception as e:
    print(f"An error occurred: {e}")
my_session.commit()
print("Hotel seeded successfully")


print("Start Seeding Bookings")
booking_list = []
for i in range(10):
    new_booking = Booking(guest_name=fake.name(), hotel_id=random.randint(1, 10))
    booking_list.append(new_booking)
try:
    my_session.add_all(booking_list)
    my_session.commit()
    print("Booking seeded successfully")
except Exception as e:
    print(f"An error occurred: {e}")
    my_session.commit()
    print("Booking seeded successfully")
   