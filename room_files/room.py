class Room:
    """
    This class represents a room with specific details.

    Attributes:
    - room_number (int): The number of the room.
    - room_name (str): The name/title of the room.
    - description (str): A brief description of the room.
    - list_all (list): A class variable to store all instances of Room.
    - room_counter (int): A class variable to keep track of room numbers.
    """

    # Class variable to store all instances
    list_all = []
    room_count = 1  # Initialize the room counter

    def __init__(self, room_number: int, room_name: str, description: str):
        """
        Initializes a Room instance with provided details.

        Args:
            :param room_name (str): The name/title of the room.
            :param description (str): A brief description of the room.
        """
        self.room_counter = Room.room_count  # Assign room number from counter
        self.room_number = room_number
        self.room_name = room_name
        self.description = description
        Room.room_count += 1  # Increment room counter
        Room.list_all.append(self)

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value: int):
        self._room_number = value

    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, value: str):
        self._room_name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def room_counter(self):
        return self._room_counter

    @room_counter.setter
    def room_counter(self, value: int):
        self._room_counter = value

    @classmethod
    def remove_room(cls, room_number):
        """Class method to remove a room based on room number."""
        for room in cls.list_all:
            if room.room_counter == room_number:
                cls.list_all.remove(room)
            else:
                f"Room {room_number} not found."

    @classmethod
    def listall(cls):
        """Class method to print details of all instances of Room."""
        for a in Room.list_all:
            print(a.__class__, a.__dict__)

    def __repr__(self):
        """Returns a string representation of the ClassRoom object."""
        return f'Room({self.room_number}, {self.room_name}, {self.description})\n'


if __name__ == '__main__':
    room1 = Room('112', '', '')
    room2 = Room('101', '', '')
    room3 = Room('119', '', '')
    Room.listall()

    Room.remove_room(2)
    room4 = Room('110', '', '')

    print()
    Room.listall()
