import json

class Data:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        with open("data.json", "r") as jsonFile:
            data = json.load(jsonFile)
        self.destination_data = data["list1"]
        return self.destination_data

    def update_destination_codes(self):
        data = {'list1': self.destination_data}
        with open('data.json', 'w') as jsonFile:
            json.dump(data, jsonFile)
