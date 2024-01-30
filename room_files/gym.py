import csv
from room_files.room import Room
from room_files.equipment import Equipment


class Gym(Room):
    """A class representing a gymnasium that inherits from the Room class."""

    # Class variable to store all instances
    list_all = []

    # constant variable representing the type of room
    TYPE_OF_ROOM = 'gymnasium'

    def __init__(self, room_number: int, room_name: str, description: str, equipment: Equipment):
        """
        Initializes a Gym object.

        :param room_number: The number associated with the gymnasium.
        :param room_name: The name of the gymnasium.
        :param description: A description of the gymnasium.
        :param equipment: An instance of the Equipment class representing the equipment in the gymnasium.
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
        Loads classroom data from a CSV file and returns a list of Gym objects.

        :param filename: The path to the CSV file containing the gymnasium data.
        :param type_of_room: The type of room to filter while loading data (default is 'gymnasium').
        :return: A list of Gym objects loaded from the file.
        """
        gymnasium_list = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['type'] == type_of_room:
                    gymnasium_list.append(Gym(int(row['room_number']), row['room_name'], row['description'],
                                              Equipment.load_from_file(filename, row['room_number'])))
        return gymnasium_list

    def __repr__(self):
        """Returns a string representation of the Gym object."""
        return f'Gym({self.room_number}, {self.room_name}, {self.description}, Equipment({self.equipment}))\n'


if __name__ == '__main__':
    print(Gym.load_from_file('/Users/nikitsya/Desktop/OOSample4/csv_data_DIFE/rooms.csv'))
