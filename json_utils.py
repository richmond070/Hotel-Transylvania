import json

def load_json(file_path):
        try:
           with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            print(f"The file {file_path} was not found")
        except json.JSONDecodeError:
            print("Error decoding JSON data")  