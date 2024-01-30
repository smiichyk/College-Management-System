import csv
from room_files.room import Room
from room_files.equipment import Equipment


class ClassRoom(Room):
    """A class representing a classroom that inherits from the Room class."""

    # class variable to store all instances
    list_all = []

    # constant variable representing the type of room
    TYPE_OF_ROOM = 'class_room'

    def __init__(self, room_number: int, room_name: str, description: str, equipment: Equipment):
        """
        Initializes a ClassRoom object.

        :param room_number: The number associated with the classroom.
        :param room_name: The name of the classroom.
        :param description: A description of the classroom.
        :param equipment: An instance of the Equipment class representing the equipment in the classroom.
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
        Loads classroom data from a CSV file and returns a list of ClassRoom objects.

        :param filename: The path to the CSV file containing the classroom data.
        :param type_of_room: The type of room to filter while loading data (default is 'class_room').
        :return: A list of ClassRoom objects loaded from the file.
        """
        class_room_list = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['type'] == type_of_room:
                    class_room_list.append(ClassRoom(int(row['room_number']), row['room_name'], row['description'],
                                                     Equipment.load_from_file(filename, row['room_number'])))
        return class_room_list

    def __repr__(self):
        """Returns a string representation of the ClassRoom object."""
        return f'ClassRoom({self.room_number}, {self.room_name}, {self.description}, Equipment({self.equipment}))\n'


if __name__ == '__main__':
    print(ClassRoom.load_from_file('/Users/nikitsya/Desktop/OOSample4/csv_data_DIFE/rooms.csv'))
