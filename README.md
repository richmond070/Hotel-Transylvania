# HOTEL TRANSYLVANIA

## INTRODUCTION

Hotel Transylvania is a hotel management system for guest to be able to book, checkIN and checkOut of a hotel and also allow management to manage the resources of the hotel.

In the HMS (Hotel Management System ) we have six (6) modules which are - user.py - guest.py - staff.py - reservation.py - room.py - reservation.py - hotel_management_system.py

## REQUIREMENTS

    ### USER
    - Login and Registration system for guest and staff
    - The class should have attributes of name, email, password, and role (Guest, Staff)
    - Simplify role of user into guest or staff

    ### STAFF
    - The Staff class should inherit from the User class
    - It should have attribute of Position (admin, manager)

    ### Guest
    - The Guest class should inherit from the User class
    - It should have attribute of checkedIn (True/False)

    ### ROOM
    - Create, update and delete rooms
    - Handle room status(vacant, occupied, under maintenance )
    - Store room details such as  room_number, room_type, price and status

    ### RESERVATION
    - Basic room booking system
    - allow guest to check for available rooms and make reservations
    - store reservation details such as reservation_id, room_number, guest_id and checkIn_date

    ### HOTEL MANAGEMENT SYSTEM (HMS)
    - Keep track of guest details (name, email, and reservation details)
    -View, update or delete guest information on reservations made

## User module

The User module is comprised of all the user information of both the staff and the guest doing this was to insure the user information is gathered in one place and the can be identified by their role of either a user or a guest

```python
class User:
    def __init__(self, user_id: str, name: str, email: str, password: str, role: str) :
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role
        self.password = password

    # Method to verify if the stored password matches the given password
    def verify_password(self, password: str) -> bool:
        return self.password == password
```

The class is initialized with attributes of user id, name, email, role and password
The verify_password function is a method to verify if the given password at login matches the registered password

```python
class AuthSystem :
    def __init__(self):

        self.users = {}
```

The AuthSystem class is initialized with an empty dictionary self.users to store all users created

## Guest module

```python
class Guest (User):
    def __init__(self, user_id: str, name: str,  password: str, email: str, checkedIn: bool):
        super().__init__(user_id, name, email, password, role = "guest")

        self.checkedIn = checkedIn
```

The guest class inherits from the user class and has an attribute of checkedIn to return a boolean value of True if the guest is checked in and false if the user is not

## Staff module

```python
class Staff (User):
    def __init__(self, user_id: str, name: str, password: str, role: str, position: str):
        super().__init__(user_id, name, password, role= "staff")
        self.position = position
```

The staff class inherits from the User class and has an attribute of position, where the position of the staff is recorded. It could be positions such as manager, admin, receptionist and so on

## Room module

```python
class Room:
    # Initializing the class
    def __init__(self, room_number: int, room_type: str, price: float, status: str = "Vacant") -> None:
        self.room = room_number
        self.room_type = room_type
        self.price = price
        self.status = status
```

In the Room module the Room class is initialized with attributes such as room_number which also serves as the room id to keep track of the rooms, room_type which could be a single, double or suite, price to set the price of the room and status of the room to determine if the room is occupied by a guest or is vacant for rent.

```python
class RoomService:
    def __init__(self) -> None:
        self.rooms = {}
```

Within the module a RoomService class is declared as well and is initialized with a self.rooms dictionary to keep track of all the room created within the hotel system. The rooms could be also updated, viewed and deleted from this dictionary as well.

## Reservation module

```python
class Reservation:
    def __init__(self, room: Room, reservation_id: int, guest: Guest, checkIn: datetime, checkOut: datetime) -> None:
        self.reservation_id = reservation_id
        self.room = room
        self.guest = guest
        self.checkIn_date = checkIn
        self.checkOut = checkOut
```

This module has a class Reservation that is initialized with the attribute of reservation_id, room which takes attributes of the Room class and is used to get the room_number, guest also takes in attributes of the Guest class and is used to get the Guest_id (user_id), checkIn to store the date a guest checked into the hotel and checkout to store the date a guest checks out of the hotel.

```python
class ReservationSystem:
    def __init__(self):
        self.users = dict(data.get('users', {}))
        self.rooms = dict(data.get('rooms', {}))
        self.reservations = {}
        self.next_reservation_id = 1
```

Also in the module another class is initialized ReservationSystem with self.users and self.rooms to get the user and rooms data that is stored in a JSON file, self.reservations is an empty dictionary to store the reservation information and self.next_reservation_id to increment the reservation_id as more details are added to the dictionary.

## Hotel_management_system module

```python
class HotelManagementSystem():

    def __init__(self):
        self.guests = {}
        self.users = dict(data.get('users', {})) # converting the user to a dict
        self.rooms = dict(data.get('rooms', {})) # converting the rooms to a dict
        self.reservation = dict(data.get('reservations', {})) # converting the reservation to a dict
        self.guest_status = data.get('guests', {})

        # to look up the status of the guest
        for user_id, user_info in self.users.items():
            # check for the role of user
            if user_info['role'] == 'guest':
               # if their is no entry for the guest it should return False
                checkedIn = self.guest_status.get(user_id, {}).get('checkedIn', False)
                # store the guest details in a dict called self.guests
                self.guests[user_id] = Guest(
                    user_id=user_id,
                    name=user_info['name'],
                    email=user_info['email'],
                    password=user_info['password'],
                    checkedIn=checkedIn
                )
```

In this module the class is initialized with an empty dictionary self.guest to store the information of the guest from the users data to be queried to perform other functions in the class, self.users, self.rooms, self.reservation, self.guest_status all retrieve the data from the JSON file to be used in the class methods.

## PACKAGES

- ### JSON:

  Imported Json for the dataset that was used in the course of the project to query data

- ### DATETIME

  Imported dateTime to use for the checkedIn attribute from the REservation module

## CONCLUSION

This project was done to test my skills in python and also DSA level of understanding, with data structures lick dictionaries and list (arrays) i was able to use and understand how to use their methods, how to convert one data structure from one to another.
