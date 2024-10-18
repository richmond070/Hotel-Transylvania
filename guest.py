""" The guest management module keeps track of guest details (e.g name, contact info)
- allows admins to view, update or delete guest information
- manage guest reservations made
- view all reservations made by a guest
"""

from user import *

class Guest (User):
    def __init__(self, user_id: str, name: str,  password: str, email: str):
        super().__init__(user_id, name, email, password, role = "guest")
        

        

