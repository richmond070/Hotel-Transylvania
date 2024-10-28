"""The Staff class / module is to represent the staff with their positions 
    - Their are three available positions: - Admin, Manager, Receptionist
    - The Admin has control over sees the staff and guest combined
    - The Manager manages the rooms and reservation details of a guest and all guest
    _ The Receptionist is in charge of guest checkIn and checkOut and also knowing of available rooms in the hotel

    - the staff class will inherit the User class and will have an attribute of "position"
"""


from user import User
from json_utils import *


#loading Json data
file_path = "data.json"
data = load_json(file_path)


# Staff class 
class Staff (User): 
    def __init__(self, user_id: str, name: str, password: str, role: str, position: str):
        super().__init__(user_id, name, password, role= "staff")
        self.position = position




    