import random


class Data1:
    def __init__(self):
        self.months = ("January", "February", "March", "April", "May", "June", "July", "August",
                       "September", "October", "November", "December")

        self.birthday_locations = {"Boat", "Backyard", "Haunted House", "My house", "The Moon", ""}

        self.sweepstakes = {1: {'id': 422, 'name': 'Paul Reevus'},
                            2: {'id': 992, 'name': 'Jim Lahey'},
                            3: {'id': 772, 'name': 'Gustavo Almaduvar'},
                            4: {'id': 777, 'name': 'Johnny Winsem'},
                            5: {'id': 817, 'name': 'Tricia Takanawa'}
                            }

        self.family_members = [{'fName': 'Paul',
                                'lName': 'Reevus',
                                'relationship': 'Brother'},
                               {'fName': 'Jim',
                                'lName': 'Lahey',
                                'relationship': 'Uncle'},
                               {'fName': 'Gustavo Almaduvar',
                                'lName': 'Almaduvar',
                                'relationship': 'Father'},
                               {'fName': 'Tricia',
                                'lName': 'Takanawa',
                                'relationship': 'Mother'},
                               {'fName': 'Johnny',
                                'lName': 'Winsem',
                                'relationship': 'Brother'}]

    def print_pi_day_month(self):
        pi_day_month = self.months[2]
        print(pi_day_month)

    def print_bday_locations(self):
        for location in self.birthday_locations:
            print(location)

    def sweepstakes_winner(self):
        print("And the winner is...")
        i = random.randint(1, 6)
        print(self.sweepstakes[i]['name'])

    def print_brothers(self):
        for member in self.family_members:
            if member['relationship'] == 'Brother':
                print("Found a brother")
