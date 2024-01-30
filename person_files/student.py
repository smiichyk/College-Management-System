import csv
from person_files.person import Person


class Student(Person):
    """
    The 'Student' class represents a student, inheriting from the `Person` class.

    Attributes:
    - student_id (int): Student ID of the student.
    - course_name (str): Name of the course the student is enrolled in.

    Methods:
    - __init__: Initializes a Student object with first_name, last_name, student_id, address, and course_name.
    - load_from_file: Loads Student instances from a specified CSV file.
    - __repr__: String representation of the Student object.
    """

    def __init__(self, first_name: str, last_name: str, student_id: int, address: str, course_name: str):
        """
        Initializes a Student object.

        :param first_name: First name of the student.
        :param last_name: Last name of the student.
        :param student_id: Student ID of the student (must be 7 digits).
        :param address: Address of the student.
        :param course_name: Name of the course the student is enrolled in.
        """
        assert len(str(student_id)) == 7, f"Student ID {student_id} must be 7 in length."
        super().__init__(first_name, last_name, address)
        self._student_id = student_id
        self.course_name = course_name

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value: int):
        self._student_id = value

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value: str):
        self._course_name = value

    @classmethod
    def load_from_file(cls, filename: str):
        """
        Loads Tutor instances from a specified CSV file.

        :param filename: The filename of the CSV file containing tutor information.
        :return: A list of Tutor instances created based on the provided data.
        """
        student_list = []
        with open(filename, newline='') as student_data:
            reader = csv.DictReader(student_data)
            for row in reader:
                student_list.append(Student(row['first_name'], row['last_name'], row['student_id'], row['address'],
                                            row['course']))
        return student_list

    def __repr__(self):
        """Returns a string representation of the Student object."""
        return f'Student({self.first_name}, {self.last_name}, {self.student_id}, {self.address}, {self.course_name})\n'


if __name__ == '__main__':
    print(Student.load_from_file('../csv_data_DIFE/student_list.csv'))
