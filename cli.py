import sys
from database import create_tables, SessionLocal
from models.Hotel import Hotel
from models.Booking import Booking
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main_menu():
    while True:
        print("\nHotel Booking System")
        print("1. Add a hotel")
        print("2. View all hotels")
        print("3. Delete a hotel")
        print("4. Add a booking")
        print("5. View all bookings")
        print("6. Delete a booking")
        print("7. Exit")

        choice = input("Enter your choice: ")

        with SessionLocal() as session:
            if choice == "1":
                name = input("Enter hotel name: ")
                location = input("Enter hotel location: ")
                try:
                    hotel = Hotel.create(session, name, location)
                    print(f"Hotel '{hotel.name}' added successfully!")
                except Exception as e:
                    print(f"Error adding hotel: {e}")

            elif choice == "2":
                hotels = Hotel.get_all(session)
                if hotels:
                    for hotel in hotels:
                        print(hotel)
                else:
                    print("No hotels found.")

            elif choice == "3":
                hotel_id = input("Enter hotel ID to delete: ")
                try:
                    if Hotel.delete(session, hotel_id):
                        print("Hotel deleted successfully.")
                    else:
                        print("Hotel not found.")
                except Exception as e:
                    print(f"Error deleting hotel: {e}")

            elif choice == "4":
                guest_name = input("Enter guest name: ")
                hotel_id = input("Enter hotel ID for booking: ")
                try:
                    booking = Booking.create(session, guest_name, hotel_id)
                    print(f"Booking for {booking.guest_name} created successfully!")
                except Exception as e:
                    print(f"Error creating booking: {e}")

            elif choice == "5":
                bookings = Booking.get_all(session)
                if bookings:
                    for booking in bookings:
                        print(booking)
                else:
                    print("No bookings found.")

            elif choice == "6":
                booking_id = input("Enter booking ID to delete: ")
                try:
                    if Booking.delete(session, booking_id):
                        print("Booking deleted successfully.")
                    else:
                        print("Booking not found.")
                except Exception as e:
                    print(f"Error deleting booking: {e}")

            elif choice == "7":
                print("Exiting system...")
                sys.exit()

            else:
                print("Invalid choice. Please try again.")

def run_tests():
    print("Running tests...")
    # Test database connection
    try:
        with SessionLocal() as session:
            session.execute("SELECT 1")
        print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")

    # Test creating a hotel
    try:
        with SessionLocal() as session:
            hotel = Hotel.create(session, "Test Hotel", "Test Location")
            print(f"Test hotel '{hotel.name}' created successfully.")
    except Exception as e:
        print(f"Failed to create test hotel: {e}")

    # Test retrieving hotels
    try:
        with SessionLocal() as session:
            hotels = Hotel.get_all(session)
            print(f"Retrieved hotels: {hotels}")
    except Exception as e:
        print(f"Failed to retrieve hotels: {e}")

if __name__ == "__main__":
    create_tables()
    main_menu()
