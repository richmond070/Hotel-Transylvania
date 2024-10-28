""" This is the room module it will have a class of Room 
The class has methods of create, update and delete rooms
The class will have attributes such as room number, type of room (single, double, suite), price of room and status of the room
"""
import json
from json_utils import *


#loading Json data
file_path = "data.json"
json_data = load_json(file_path)


#This is the Room class
class Room: 
    # Initializing the class
    def __init__(self, room_number: int, room_type: str, price: float, status: str = "Vacant") -> None:
        self.room = room_number
        self.room_type = room_type
        self.price = price
        self.status = status



# This class handles the create, delete and update room
class RoomService:
    def __init__(self) -> None:
        self.rooms = {}



    # Create room
        """This method we first look to is if the room_number exist in the self.rooms dictionary
        - If it exist it returns False
        - If not the Room details are added to the dictionary
        """
    def createRoom (self, room_number: int, room_type: str, price: float):
        if room_number in self.rooms:
            print(f"Room {room_number} already exist")
            return False
        self.rooms[room_number] = Room(room_number, room_type, price )
        print(f"A {room_type} has been added!!")
        return True

    #Update room 
    """ In this method we access the dictionary with the room_number 
        - Then we check if the room_number exist
        - If it does not exist we return False
        - If it exist the room_number is returned 

        - The status of the room is checked 
        - If the value is not within "vacant", "occupied", "under maintenance" it prints an INvalid status
    """
    def updateRoom (self, room_number: int, status: str = None, price: float = None):
        # Check if room exist 
       if room_number not in self.rooms:
           print(f"Room {room_number} not found")
           return False 
       room = self.rooms[room_number]

       # Update the room status if provided
       if status:
           if status in ["vacant", "occupied", "under maintenance"]:
               room.status =status
               print(f"Room {room_number} status updated to {status}")
           else:
                print(f"Invalid status: {status}")
               
        #update the room price if provided
       if price:
           room.price = price
           print(f"Room {room_number} price updated to {price}")
       return True
    

    # Method to delete room details
    def delete_room (self, room_number):
        if room_number in self.rooms:
           del self.rooms[room_number]
           print(f"Room {room_number} has been taken out")
           return True
        else:
            print(f"Room {room_number} not found")
            return False


    # Method to display room details
    """This method is also access using the room_number 
    - If the room does not exist it returns false
    - If the room_ number exist it prints the details of the room
    """
    def display_room(self, room_number: int):
        # search for the room
        if room_number not in self.rooms:
            # If not found
            print(f"Room {room_number} not found")
            return
        # Else return the room details
        room = self.rooms[room_number]
        print(f"Room {room_number}: Type: {room.room_type}, Price: {room.price}, Status: {room.status}")

    # Method to display all rooms 
    def display_rooms (self):
        if not self.rooms:
            print("No rooms available")
        else:
            for room_number, room in self.rooms.items():
                print(f"Room {room_number} is a {room.room_type} bed room that goes for {room.price} it is currently {room.status}")
        return self.rooms
       



room_system = RoomService()

room_system.createRoom(101, "single", 20.0)
room_system.createRoom(102, "double", 20.0)
room_system.createRoom(103, "single", 20.0)

room_system.display_room(101)

room_system.updateRoom(101, "occupied")
room_system.updateRoom(102, price=40.0)
room_system.updateRoom(103, "vacant")

#room_system.delete_room(103)

room_system.display_room(102)
room_system.display_room(103)

room_system.display_rooms()