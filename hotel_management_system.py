""" - guest will have a checkedIn attribute which will be a boolean value 
        (if true; guest is checkedIn to their reservation if it is false guest is checkedOut)
    - method to view, update or delete guest information on reservations 
    
"""


from datetime import datetime
from reservation import Reservation
from room import Room
from staff import Staff
from guest import Guest
from json_utils import *


#loading Json data
file_path = "data.json"
data = load_json(file_path)


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
        #print(f" guest status = {self.guest_status}")

    # Method to retrieve user information and checkIn status
        
    def get_guest_information(self):
        guest_info = [] # List to store the user details and their checked in status
        # Retrieve the guest details from the self.guest dictionary
        for user_id, guest in self.guests.items():
            # Addend the details into a list 
            guest_info.append({
                'user_id': guest.user_id,
                'name': guest.name,
                'email': guest.email,
                'checkedIn': guest.checkedIn
            })
        print(f"guest info = {guest_info}")
        return guest_info


    # Method to update a guest information
    def update_checkIn_status(self, user_id: int):
        """ - first check if the user_id is in the self.guests dict
            - check if the have a reservation
            - if their is a reservation update the status to True 
            - if not return 'no reservation found'
        """
       
       # Find the guest
        guest = self.guests.get(str(user_id)) 
        print(guest)  
        if guest :
            print(f"guest with Id {user_id} found")  
            
            # find reservation of the guest using a comprehensive list
            reservation = [
                guest_id for guest_id, guest in self.reservation.items()
                if guest['user_id'] == user_id and guest['room_number']
            ]
            #print(f'guest {user_id} has a reservation {reservation}')

            if reservation:
                self.guests.update([('checkedIn', True)])
                print(f"guest {user_id} has been checked in")
                return self.guests
            else:
                print(f" Guest {user_id} does not have any reservation")
                return None
        else: 
            print(f"Guest not found ")
            return False


    # method to delete guest reservation
    def delete_reservation(self, user_id: int):
        """ - first check if the user_id is in the self.guests dict
            - check if the guest has any reservations
            - if the do store the details in a list
            - if their is a reservation delete the reservation 
            - if not return 'no reservation found'
        """
       
       # Find the guest
        guest = self.guests.get(str(user_id)) 
        print(guest)  
        # if guest exist 
        if guest :
            print(f"guest with Id {user_id} found")  
            
            # find all the reservations made by the guest with their id and pass it to a list
            booked = [
                checkedIn for checkedIn, guest in self.reservation.items()
                if guest['user_id'] == user_id 
            ]
            print(booked)
            
            if booked: 
                # Ideally the last id on the list is the current reservation made my the guest
                room_out = booked[-1]
                # Remove the last id from the list 
                self.reservation.pop(room_out)
                print(f"Reservation has been cancelled")
                return self.reservation
            else:
                print(f" Guest {user_id} does not have any reservation")
                return None
        else: 
            print(f"Guest not found ")
            return False
        
    # Method to find a specific user and return all their details of the user
    def find_guest_details(self, user_id):
        """- How to retrieve the users details
        - get the user_id and check for it in the self.user dict and return the user details
        - search the reservation to see if the user/ guest has any reservations made and return the details of the reservation
        """

        # Find if the ID provided matches any ID in the database
        user = self.users.get(str(user_id))



        # Check if the user has a role of guest
        if user and user['role'] == 'guest':
            # get the name and email of the guest
            user_name = user['name']
            email = user['email']
            #print(f" Name: {user_name}; email: {email} ") 

            guest = self.guest_status.get(str(user_id))
            check_in_status = guest.get('checkedIn') if guest else False

                        # Check if the guest has any reservations made
            for reservation_id, details in self.reservation.items():
                # check if the user_id matches any of the user_id in the reservation table
                if isinstance(details, dict) and details['user_id'] == user_id:
                    #print(details)
                    print(f"""
    Details for {user_name}:
    - Email: {email}
    - Room Number: {details['room_number']}
    - Checked-In Date: {details['checkedIn']}
    - Checked-In Status: {'Checked In' if check_in_status else 'Not Checked In'}
    """)
            return True

        return False
                
                
            





hms = HotelManagementSystem()

#hms.get_guest_information()
#hms.update_checkIn_status(2)
#hms.update_checkIn_status(9)
#hms.delete_reservation(10)
#hms.delete_reservation(4)
hms.find_guest_details(4)