""" The reservation module is a basic booking system for guest 
- It would allow guest to check for room availability 
- store reservation information like check in and check out dates and guest details as well 
- The reservation class will have attributes of checkIn and checkOut

- The room.py module is going to be imported and used as a parent class for the reservation class
"""


from room import Room
from room import RoomService
from guest import Guest
from datetime import datetime
import json

# Declaration of the reservation class
"""For the ReservationSystem we would have 
- add a checkIn date and a checkOut date
- update your reservation details
- delete your reservation details
- display reservation details

* Attributes of the booking system

- booking_id
- checkIn date
- checkOut date
- guest_id
- 
"""

class Booking: 
    def __init__(self, room: Room, booking_id: int, guest: Guest, checkIn: datetime, checkOut: datetime) -> None:
        self.booking_id = booking_id
        self.room = room
        self.guest = guest
        self.checkIn = checkIn
        self.checkOut = checkOut


class BookingSystem:
    def __init__(self, room_service) -> None:
        self.booking = {} # dictionary to store booking_id
        self.next_reservation_id = 1 # Auto-increment reservation ID
        self.room_service = room_service

    """ Method to add available rooms
    - First find the rooms 
    - Then if their is any room that is vacant the room should be added to the list of available rooms
    """
    def available_rooms (self):
        # Get the rooms from the instance
        rooms = self.room_service.display_rooms()

        #print("Rooms returned from display rooms():", rooms)

        # List to store vacant rooms
        vacant_rooms = []

        # Checking if rooms is not NOne before accessing .items()
        if rooms is not None: 
            #filter and collect only vacant rooms
            for room_number, room in rooms.items():
                if room.status == 'vacant':
                    vacant_rooms.append((room_number, room))
                    # Check if there are any vacant rooms to display
            if vacant_rooms:
                for room_number, room in vacant_rooms:
                    print(f"Room {room_number} is a {room.room_type} bed room that goes for {room.price} it is currently {room.status}")
            else:
            # No vacant rooms available
                print("No vacant rooms available.")
        else: 
            print(f"No rooms available")
                
    

if __name__ == "__main__":
    m_system = RoomService()

m_system.load_rooms_from_json('room.json')

booking = BookingSystem(m_system)

booking.available_rooms()
