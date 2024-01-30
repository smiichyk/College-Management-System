from person_files.student import Student
from course_files.module import Module


class Course:
    """Class represents a course within a curriculum, managing its students, modules, and related information."""

    # Class variable to store all instances of Course
    list_all = []

    def __init__(self, course_name: str, description: str):
        """
        Initializes a Course object.

        :param course_name: Name of the course.
        :param description: Description of the course.
        """
        self.course_name = course_name
        self.description = description

        self.student_list = []
        self.module_list = []
        self.tutor_filename = ''
        Course.list_all.append(self)

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value: str):
        self._course_name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def student_list(self):
        return self._student_list

    @student_list.setter
    def student_list(self, value: list or str):
        """
        Setter method for student_list property.

        If the value is a list, it sets the student_list directly.
        If the value is a string, it loads students from a file and filters students belonging to the course.

        :param value: Either a list of Student objects or a filename to load students from.
        """
        if isinstance(value, list):
            self._student_list = value
        elif isinstance(value, str):
            student_list = []
            for student in Student.load_from_file(value):
                if student.course_name == self.course_name:
                    student_list.append(student)
            self._student_list = student_list

    @property
    def module_list(self):
        return self._module_list

    @module_list.setter
    def module_list(self, value: list or str):
        """
        Setter method for module_list property.

        If the value is a list, it sets the module_list directly.
        If the value is a string, it loads modules from a file and filters modules belonging to the course.

        :param value: Either a list of Module objects or a filename to load modules from.
        """
        if isinstance(value, list):
            self._module_list = value
        elif isinstance(value, str):
            module_list = []
            for module in Module.load_from_file(value, self.tutor_filename):
                if module.course_name == self.course_name:
                    module_list.append(module)
            self._module_list = module_list

    @property
    def tutor_filename(self):
        return self._tutor_filename

    @tutor_filename.setter
    def tutor_filename(self, new_tutor_filename):
        self._tutor_filename = new_tutor_filename

    def add_student(self, student: Student):
        """
        Add a student to the student list of the course.

        :param student: Student object to be added to the course.
        """
        self.student_list.append(student)

    def add_module(self, module: Module):
        """
        Add a module to the module list of the course.

        :param module: Module object to be added to the course.
        """
        self.module_list.append(module)

    @classmethod
    def listall(cls):
        """Class method to print details of all instances of Course."""
        for a in Course.list_all:
            print(a.__class__, a.__dict__)

    def __repr__(self):
        """Returns a string representation of the Course object."""
        return (f'Course({self.course_name}, {self.description}, {len(self.module_list)} modules, '
                f'{len(self.student_list)} students)\n')


if __name__ == '__main__':
    course = Course('Software Development', 'description')
    course.tutor_filename = '/csv_data_DIFE/tutor.csv'
    course.module_list = '/Users/nikitsya/Desktop/OOSample4/csv_data_DIFE/modules.csv'
    course.student_list = '/Users/nikitsya/Desktop/OOSample4/csv_data_DIFE/student_list.csv'

    print(course.list_all)
