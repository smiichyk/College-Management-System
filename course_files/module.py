import csv
from person_files.tutor import Tutor


class Module:
    """
    The 'Module' class contains information about the subjects in a course.

    Attributes:
    - module_name (str): Name of the module.
    - course_tutor (Tutor or str): Tutor object or name of the course tutor.
    - course_name (str): Name of the course.

    Class Variables:
    - list_all (list): A list containing all instances of Module.

    Methods:
    - __init__: Initializes a Module object with module_name, course_tutor, and course_name.
    - load_from_file: Loads Module instances from a specified module CSV file and tutor CSV file.
    - listall: Prints details of all instances of Module.
    """

    # Class variable to store all instances of Module
    list_all = []

    def __init__(self, module_name: str, course_tutor: Tutor or '', course_name: str):
        """
        Initializes a Module object.

        :param module_name: Name of the module.
        :param course_tutor: Tutor object or name of the course tutor.
        :param course_name: Name of the course.
        """
        self.module_name = module_name
        self.course_tutor = course_tutor
        self.course_name = course_name
        Module.list_all.append(self)

    @property
    def module_name(self):
        return self._module_name

    @module_name.setter
    def module_name(self, value: str):
        self._module_name = value

    @property
    def course_tutor(self):
        return self._course_tutor

    @course_tutor.setter
    def course_tutor(self, value: str):
        self._course_tutor = value

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value: str):
        self._course_name = value

    @classmethod
    def load_from_file(cls, module_filename: str, tutor_filename: str):
        """
        Loads Module instances based on data loaded from specified CSV files.

        This method reads information from CSV files to create Module instances.
        It matches modules with tutors based on shared subjects and creates Module objects accordingly.

        CSV file format expectations:
        - The module_filename should have 'course_name' and 'course_subjects' columns.
        - The tutor_filename should contain relevant information required for Tutor.load_from_file method.

        :param module_filename: The filename of the CSV file containing module information.
        :param tutor_filename: The filename of the CSV file containing tutor information.
        :return: A list of Module instances created based on the provided data.
        """
        module_dict = {}
        module_list = []
        unique_modules = {}

        tutor_list = Tutor.load_from_file(tutor_filename)
        module_and_course_list = []

        with open(module_filename, newline='') as module_data:
            reader = csv.DictReader(module_data)
            for row in reader:
                course_name = row['course_name']
                course_subjects = [part.strip(" '") for part in row['course_subjects'].split(',')]
                module_dict[course_name] = course_subjects

        for course_name, modules in module_dict.items():
            for module in modules:
                module_and_course_list.append([course_name, module])

        for tutor in tutor_list:
            for value in module_and_course_list:
                if value[1] in tutor.subjects:
                    module_key = (value[1], value[0])
                    if module_key not in unique_modules:
                        module_list.append(Module(value[1], tutor, value[0]))
                        unique_modules[module_key] = True

        for value in module_and_course_list:
            module_key = (value[1], value[0])
            if module_key not in unique_modules:
                module_list.append(Module(value[1], '', value[0]))
                unique_modules[module_key] = True

        return module_list

    @classmethod
    def listall(cls):
        """Class method to print details of all instances of Module."""
        for a in Module.list_all:
            print(a.__class__, a.__dict__)

    def __repr__(self):
        """Returns a string representation of the Module object."""
        return (f'Module({self.module_name}, Tutor('
                f'{self.course_tutor.last_name if type(self.course_tutor) == Tutor else self.course_tutor}), '
                f'{self.course_name})\n')


if __name__ == '__main__':
    Module.load_from_file('/csv_data_DIFE/modules.csv',
                          '/csv_data_DIFE/tutor.csv')

    print(Module.list_all)
