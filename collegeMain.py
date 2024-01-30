from course_files.course import Course
from college import College
from room_files.class_room import ClassRoom
from room_files.gym import Gym
from room_files.hall import Hall
from room_files.equipment import Equipment


ROOMS_PATH = '/Users/nikitsya/Desktop/-/OOSample4/csv_data_DIFE/rooms.csv'


def software_development_course():
    """
    Create a 'Software Development' course.

    :return: Course object representing 'Software Development'.
    """
    course = Course('Software Development', 'description1')
    course.tutor_filename = 'csv_data_DIFE/tutor.csv'
    course.module_list = 'csv_data_DIFE/modules.csv'
    course.student_list = 'csv_data_DIFE/student_list.csv'
    return course


def games_development_course():
    """
    Create a 'Games Development' course.

    :return: Course object representing 'Games Development'.
    """
    course = Course('Games Development', 'description2')
    course.tutor_filename = 'csv_data_DIFE/tutor.csv'
    course.module_list = 'csv_data_DIFE/modules.csv'
    course.student_list = 'csv_data_DIFE/student_list.csv'
    return course


def law_with_criminology_course():
    """
    Create a 'Law with Criminology' course.

    :return: Course object representing 'Law with Criminology'.
    """
    course = Course('Law with Criminology', 'description3')
    course.tutor_filename = 'csv_data_DIFE/tutor.csv'
    course.module_list = 'csv_data_DIFE/modules.csv'
    course.student_list = 'csv_data_DIFE/student_list.csv'
    return course


def classrooms():
    return ClassRoom.load_from_file(ROOMS_PATH)


def gyms():
    return Gym.load_from_file(ROOMS_PATH)


def halls():
    return Hall.load_from_file(ROOMS_PATH)


def new_class_room():
    return ClassRoom('', '', '', Equipment({'': ''}))


if __name__ == '__main__':
    DIFE = College('DIFE')
    print(DIFE)

    DIFE.add_course(software_development_course())
    DIFE.add_course(games_development_course())
    DIFE.add_course(law_with_criminology_course())
    print(DIFE)

    DIFE.classroom_list = classrooms()
    DIFE.gym_list = gyms()
    DIFE.hall_list = halls()
    print(DIFE)

    DIFE.add_classroom(new_class_room())
    print(DIFE)

    DIFE.remove_classroom(None, 108)
    DIFE.remove_hall(None, 121)
    DIFE.remove_gym(None, 124)
    print(DIFE)
