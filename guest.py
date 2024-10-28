""" The guest management module keeps track of guest details (e.g name, contact info)
    - allows admins to view, update or delete guest information
    - guest will have a checkedIn attribute which will be a boolean value 
        (if true; guest is checkedIn to their reservation if it is false guest is checkedOut)
    - manage guest reservations made 
        ( view all reservations made by a guest both passed and present with their reservation status)
"""

from user import *
from json_utils import *


#loading Json data
file_path = "data.json"
data = load_json(file_path)

class Guest (User):
    def __init__(self, user_id: str, name: str,  password: str, email: str, checkedIn: bool):
        super().__init__(user_id, name, email, password, role = "guest")
        
        self.checkedIn = checkedIn


