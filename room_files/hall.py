import csv
from room_files.room import Room
from room_files.equipment import Equipment


class Hall(Room):
    """A class representing a hall that inherits from the Room class."""

    # Class variable to store all instances
    list_all = []

    # constant variable representing the type of room
    TYPE_OF_ROOM = 'hall'

    def __init__(self, room_number: int, room_name: str, description: str, equipment: Equipment):
        """
        Initializes a Gym object.

        :param room_number: The number associated with the hall.
        :param room_name: The name of the hall.
        :param description: A description of the hall.
        :param equipment: An instance of the Equipment class representing the equipment in the hall.
        """
        super().__init__(room_number, room_name, description)
        self.equipment = equipment

    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, value: Equipment):
        self._equipment = value

    @classmethod
    def load_from_file(cls, filename: str, type_of_room=TYPE_OF_ROOM):
        """
        Loads classroom data from a CSV file and returns a list of Hall objects.

        :param filename: The path to the CSV file containing the hall data.
        :param type_of_room: The type of room to filter while loading data (default is 'hall').
        :return: A list of Hall objects loaded from the file.
        """
        hall_list = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['type'] == type_of_room:
                    hall_list.append(Hall(int(row['room_number']), row['room_name'], row['description'],
                                          Equipment.load_from_file(filename, row['room_number'])))
        return hall_list

    def __repr__(self):
        """Returns a string representation of the Hall object."""
        return f'Hall({self.room_number}, {self.room_name}, {self.description}, Equipment({self.equipment}))\n'


if __name__ == '__main__':
    print(Hall.load_from_file('/Users/nikitsya/Desktop/OOSample4/csv_data_DIFE/rooms.csv'))
