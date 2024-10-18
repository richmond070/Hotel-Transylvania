""" creating a person class with the attributes of name, password, id_number,
The person class would be attributed to both the Guest and Staff
The user module will  have a registration class and a login class
"""
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


# Class to handle authentication logic
class AuthSystem :
    def __init__(self):

        self.users = {}

    # Register a new user
    def register(self, user_id: str, name: str, email:str, role: str, password: str):
        if name in self.users: 
            print (f"User {name} already exist!")
            return False
        self.users[user_id] = User(user_id, name, email, role, password)
        print(f"User {name} registered successfully")
        return True
    
    # Login a registered User
    def login (self, user_id: str, name: str, password:str):
        user = self.users.get(user_id)
        if not user: 
            print ("User not found")
            return False
        if user.verify_password(password):
            print(f"Login successful! Welcome {name}")
            return True
        else: 
            print("Incorrect password!")
            return False
        
    # Display registered users 
    def display_users(self):
        for user_id, user in self.users.items():
            print(f"Name: {user.name}, Role: {user.role}")
        return self.users



auth_system = AuthSystem()

auth_system.register(1, "Ahmed", "ahmed@gmail.com","password123", "guest")
auth_system.register(2, "John", "John@gmail.com","adminPass", "admin")

auth_system.login(1, "guest1", "password123")
auth_system.login(1,"guest1", "wrongPassword")

auth_system.display_users()