import csv
from person_files.person import Person


class Tutor(Person):
    """
    The 'Tutor' class represents an instructor or teacher, inheriting from the 'Person' class.

    Attributes:
    - role (str): Role or position of the tutor.
    - subjects (list): List of subjects the tutor is capable of teaching.

    Methods:
    - __init__: Initializes a Tutor object with first_name, last_name, address, role, and subjects.
    - add_subject: Adds a subject to the tutor's list of subjects.
    - load_from_file: Loads Tutor instances from a specified CSV file.
    - __repr__: String representation of the Tutor object.
    """

    def __init__(self, first_name: str, last_name: str, address: str, role: str, subjects: list or None):
        """
        Initializes a Tutor object.

        :param first_name: First name of the tutor.
        :param last_name: Last name of the tutor.
        :param address: Address of the tutor.
        :param role: Role or position of the tutor.
        :param subjects: List of subjects the tutor is capable of teaching.
        """
        super().__init__(first_name, last_name, address)
        self.role = role
        self.subjects = subjects

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, value: list):
        self._subjects = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value: str):
        self._role = value

    def add_subject(self, subject: str):
        """Adds a subject to the tutor's list of subjects."""
        self.subjects.append(subject)

    @classmethod
    def load_from_file(cls, filename: str) -> list:
        """
        Loads Tutor instances from a specified CSV file.

        :param filename: The filename of the CSV file containing tutor information.
        :return: A list of Tutor instances created based on the provided data.
        """
        tutor_list = []
        with open(filename, newline='') as tutor_data:
            reader = csv.DictReader(tutor_data)
            for row in reader:
                subjects = [part.strip(" '") for part in row['subjects'].split(',')]
                tutor_list.append(Tutor(row['first_name'], row['last_name'], row['address'], row['role'], subjects))
        return tutor_list

    def __repr__(self):
        """Returns a string representation of the Tutor object."""
        return f'Tutor({self.first_name}, {self.last_name}, {self.address}, {self.role}, {self.subjects})\n'


if __name__ == '__main__':
    print(Tutor.load_from_file('../csv_data_DIFE/tutor.csv'))
