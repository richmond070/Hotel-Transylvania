""" The reservation module is a basic booking system for guest 
- It would allow guest to check for room availability 
- store reservation information like check in and check out dates and guest details as well 
- The reservation class will have attributes of checkIn and checkOut

- The room.py module is going to be imported and used as a parent class for the reservation class
"""


from room import *
from guest import Guest
from datetime import datetime
from json_utils import *


#loading Json data
file_path = "data.json"
data = load_json(file_path)


# Declaration of the reservation class
"""For the ReservationSystem we would have 
- add a checkIn date and a checkOut date
- update your reservation details
- delete your reservation details
- display reservation details

* Attributes of the booking system

- reservation_id
- checkIn date
- checkOut date
- guest_id
- 
"""

class Reservation: 
    def __init__(self, room: Room, reservation_id: int, guest: Guest, checkIn: datetime, checkOut: datetime) -> None:
        self.reservation_id = reservation_id
        self.room = room
        self.guest = guest
        self.checkIn_date = checkIn
        self.checkOut = checkOut


class ReservationSystem:
    def __init__(self):
        self.users = dict(data.get('users', {}))  # Convert to regular dict
        self.rooms = dict(data.get('rooms', {}))  # Convert to regular dict
        self.reservations = {}  # To store reservations
        self.next_reservation_id = 1 # Auto-increment reservation ID

       
    
    """ Method to find available rooms
    - First find the rooms 
    - Then if their is any room that is vacant the room should be added to the list of available rooms
    """

    def available_rooms(self):
        # List to store vacant rooms
        vacant_rooms = []

        # Checking if rooms is not None and not empty
        if self.rooms:
            # Filter and collect only vacant rooms
            for room_number, room in self.rooms.items():
                if room['status'] == 'vacant':
                    vacant_rooms.append((room_number, room))
            
            # Check if there are any vacant rooms to display
            if vacant_rooms:
                for room_number, room in vacant_rooms:
                    print(f"Room {room_number} is a {room.get('room_type', 'N/A')} bed room that goes for {room.get('price', 'N/A')}. It is currently {room['status']}.")
            else:
                # No vacant rooms available
                print("No vacant rooms available.")
        else: 
            print("No rooms available")


    # Method to reserve a room for a guest
            
    def reserved_room(self, user_id: int, room_type: str):
        """ How is a guest going to be able to reserver a room
       - find the guest_id: user_id
       - if the user exist we return the name of the user
       - find the room type
       - pass available room_numbers that are of the type and are vacant into a list 
       - and pass the first vacant room on the list  to the user and remove it from the list
       - store user and room in a dictionary
       """
        #print(f"Received User ID: {user_id}, Preferred Room Type: {room_type}")

        # Find the user
        user = self.users.get(str(user_id))
        
        if user and user['role'] == 'guest':
            user_name = user['name']
            print(f"Guest {user_name} requesting for a {room_type} room .")
            
           # Find the room type
            # Pass available room_numbers that are of the type and are vacant into a list
            available_rooms = [
                room_number for room_number, room in self.rooms.items() 
                if room['status'] == 'vacant' and room['room_type'].lower() == room_type.lower()
            ]
            #print(f"available_rooms: {available_rooms}")
            if available_rooms:
                # Pass the first vacant room on the list to the user and remove it from the list
                assigned_room = available_rooms[0]
                self.rooms[assigned_room]['status'] = 'occupied'

                
                # Store user and room in the reservations dictionary with a booking ID
                booking_id = self.next_reservation_id
                check_in_date = datetime.now().strftime("%Y-%m-%d")
                self.reservations[booking_id] = {
                    'user_id': user_id,
                    'room_id': assigned_room,
                    'checkedIn': check_in_date
                }
                self.next_reservation_id += 1  # Increment the reservation ID for the next booking
                
                #print(f"Booking successful! Booking ID: {booking_id}")
                print(self.reservations)
                print(f"Room {assigned_room} ({room_type}) has been reserved for {user_name}.")
                return self.reservations
            else:
                print(f"Sorry, no {room_type} rooms are currently available.")
        else:
            print(f"User ID {user_id} is not a valid guest.")


    # Method to check out a guest
    def check_out_guest(self):
        pass




if __name__ == "__main__":
    m_system = RoomService()

#m_system.load_rooms_from_json('data.json')

booking = ReservationSystem()

booking.available_rooms()
booking.reserved_room(4, 'double')
booking.reserved_room(6, 'double')
booking.reserved_room(7, 'double')
booking.reserved_room(9, 'double')
booking.available_rooms()
#booking.checkIn_checkOut(1)