from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database setup
DATABASE_URL = "sqlite:///hotel_bookings.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = session()

Base = declarative_base()
