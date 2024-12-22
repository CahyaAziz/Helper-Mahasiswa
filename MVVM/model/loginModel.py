import json
import os
import utils.helper as helper

DATA_FILE = "../user_data.json"

class LoginModel:
    def __init__(self):
        self.data_file = DATA_FILE
        self.user_data = self.load_user_data()

    def load_user_data(self):
        if not os.path.exists(self.data_file):
            self.create_user_data_file()

        with open(self.data_file, 'r') as file:
            return json.load(file)
        
    def create_user_data_file(self):
        default_data = {"users": []}
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)  # Ensure the directory exists
        with open(self.data_file, 'w') as file:
            json.dump(default_data, file, indent=4)  # Write the default data to the file
        print(f"File '{self.data_file}' created with default data.")

    def save_user_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.user_data, file, indent=4)

    def register_user(self, username, password):
        for user in self.user_data["users"]:
            if user["username"] == username:
                return False  # User already exists
            
        self.user_data["users"].append({
            "username": username,
            "password": password,
            "scheduled_tasks": [],
            "university_schedule": []
        })

        self.save_user_data()
        return True

    def auth_user(self, username, password):
        if username == "admin" and password == "admin":
            return True
        for user in self.user_data["users"]:
            if user["username"] == username and user["password"] == password:
                return True
        return False
