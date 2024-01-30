import csv


class Equipment:
    """Represents a collection of various equipments and their quantities for the room."""

    def __init__(self, equipments: dict):
        """
        Initializes an Equipment object.

        :param equipments: A dictionary containing equipment names as keys and their quantities as values.
        """
        self.equipments = equipments

    @property
    def equipments(self):
        return self._equipments

    @equipments.setter
    def equipments(self, value: dict):
        self._equipments = value

    def add_or_updates_equipment(self, equipment: str, quantity: int or str):
        """
        Adds new equipment or updates the quantity of existing equipment.

        :param equipment: Name of the equipment.
        :param quantity: Quantity of the equipment.
        """
        self._equipments[equipment] = quantity

    def remove_equipment(self, equipment: str):
        """
        Removes equipment from the collection.

        :param equipment: Name of the equipment to be deleted.
        """
        if equipment in self._equipments.keys():
            del self._equipments[equipment]
        else:
            print('There is no such equipment.')

    @classmethod
    def load_from_file(cls, filename: str, room_number: int):
        """
        Load equipment data from a CSV file for a specific room number.

        :param filename: Name of the CSV file containing equipment data.
        :param room_number: Room number to filter the equipment data.
        :return: Dictionary containing equipment names and quantities for the specified room number.
        """
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                equipment_dict = {}
                if row['room_number'] == room_number:
                    for equipment in row['equipment'].split(','):
                        key, value = equipment.split(':')
                        equipment_dict[key] = value
                    return equipment_dict

    def __repr__(self):
        """Returns a string representation of the Equipment object."""
        return f'Equipments({self.equipments})\n'


if __name__ == '__main__':
    equipment_for_room = Equipment(
        {'seating_rows': 120, 'podium': 1, 'projector': 3, 'sound_system': 1, 'lecture_materials': 'assorted'})

    # adds new equipment:
    equipment_for_room.add_or_updates_equipment('new_equipment', 3)

    # updates the quantity of existing equipment:
    equipment_for_room.add_or_updates_equipment('seating_rows', 150)

    # deletes equipment from the collection:
    equipment_for_room.remove_equipment('podium')

    print(equipment_for_room)

    print(Equipment.load_from_file('/csv_data_DIFE/rooms.csv',
                                   '101'))
