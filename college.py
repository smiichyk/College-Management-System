from course_files.course import Course
from room_files.class_room import ClassRoom
from room_files.gym import Gym
from room_files.hall import Hall


class College:
    """A class representing a college institution."""

    def __init__(self, college_name: str):
        """
        Initializes a College object.

        :param college_name: The name of the college.
        """
        self.college_name = college_name
        self.courses = []
        self.classroom_list = []
        self.gym_list = []
        self.hall_list = []

    @property
    def college_name(self):
        return self._college_name

    @college_name.setter
    def college_name(self, value: str):
        self._college_name = value

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, value: list):
        self._courses = value

    @property
    def classroom_list(self):
        return self._classroom_list

    @classroom_list.setter
    def classroom_list(self, value: list):
        self._classroom_list = value

    @property
    def gym_list(self):
        return self._gym_list

    @gym_list.setter
    def gym_list(self, value: list):
        self._gym_list = value

    @property
    def hall_list(self):
        return self._hall_list

    @hall_list.setter
    def hall_list(self, value: list):
        self._hall_list = value

    def add_course(self, course: Course):
        """
        Adds a course to the college's course list.

        :param course: The Course object to be added.
        """
        self.courses.append(course)

    def remove_course(self, course: Course):
        """
        Removes a course from the college's course list.

        :param course: The Course object to be removed.
        """
        self.courses.remove(course)

    def add_classroom(self, class_room: ClassRoom):
        """
        Adds a classroom to the college's classroom list.

        :param class_room: The ClassRoom object to be added.
        """
        self.classroom_list.append(class_room)

    def remove_classroom(self, class_room: ClassRoom or None, room_number: int or None):
        """
        Removes a classroom from the college's classroom list.

        :param class_room: The ClassRoom object to be removed (optional).
        :param room_number: The room number of the classroom to be removed (optional).
        """
        if class_room is not None:
            self.classroom_list.remove(class_room)
        elif room_number is not None:
            for classroom in self.classroom_list:
                if classroom.room_number == room_number:
                    self.classroom_list.remove(classroom)

    def add_gym(self, gym: Gym):
        """
        Adds a gym to the college's gym list.

        :param gym: The Gym object to be added.
        """
        self.gym_list.append(gym)

    def remove_gym(self, gym: Gym or None, room_number: int or None):
        """
        Removes a gym from the college's gym list.

        :param gym: The Gym object to be removed (optional).
        :param room_number: The room number of the gym to be removed (optional).
        """
        if gym is not None:
            self.gym_list.remove(gym)
        elif room_number is not None:
            for gym in self.gym_list:
                if gym.room_number == room_number:
                    self.gym_list.remove(gym)

    def add_hall(self, hall: Hall):
        """
        Adds a hall to the college's hall list.

        :param hall: The Hall object to be added.
        """
        self.hall_list.append(hall)

    def remove_hall(self, hall: Hall or None, room_number: int or None):
        """
        Removes a hall from the college's hall list.

        :param hall: The Hall object to be removed (optional).
        :param room_number: The room number of the hall to be removed (optional).
        """
        if hall is not None:
            self.hall_list.remove(hall)
        elif room_number is not None:
            for hall in self.hall_list:
                if hall.room_number == room_number:
                    self.hall_list.remove(hall)

    def __repr__(self):
        """Returns a string representation of the college object."""
        return (f'College({self.college_name}, {len(self.courses)} courses, {len(self.classroom_list)} class rooms, '
                f'{len(self.gym_list)} gyms, {len(self.hall_list)} halls)')
