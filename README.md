# Hotel Booking System

The Hotel Booking System is a Python-based Command Line Interface (CLI) application that allows users to manage hotels and bookings efficiently. Built using Python and SQLAlchemy ORM, the system enables users to add hotels, create bookings, view reservations, and manage data seamlessly through a simple interactive CLI.

## Key Features
- **Hotel Management**: Add, view, search, and delete hotels.
- **Booking System**: Create, view, and delete hotel bookings.
- **One-to-Many Relationship**: A hotel can have multiple bookings.
- **Database Integration**: Uses SQLite with SQLAlchemy ORM.

## Requirements
- Python 3.x
- SQLAlchemy

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r Pipfile
   ```

## Usage
1. Run the application:
   ```bash
   python cli.py
   ```

2. Follow the on-screen instructions to manage hotels and bookings.

## Testing the Application
To test the Hotel Booking System, you can use the built-in testing functionality in the CLI.

1. Run the application:
   ```bash
   python cli.py
   ```

2. Select the "Run Tests" option from the menu to check the system's functionality. This will:
   - Verify the database connection.
   - Create a test hotel and confirm it was added successfully.
   - Retrieve and display all hotels to ensure the application is working correctly.

## License
This project is licensed under the MIT License.
