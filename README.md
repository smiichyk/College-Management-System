# Project Title: Course Management System

## Project Overview

The Course Management System is designed to manage various aspects of an educational curriculum, including courses, students, modules, tutors, and rooms. This system supports the creation, modification, and retrieval of information related to these entities, providing a comprehensive solution for educational institutions.

## Features

- **Course Management**: Create, update, and manage courses with related information.
- **Student Management**: Add, update, and manage students enrolled in courses.
- **Module Management**: Manage course modules and assign tutors to them.
- **Tutor Management**: Add and manage tutors with their subjects and roles.
- **Room Management**: Manage different types of rooms such as classrooms, gyms, and halls with their equipment.

## Project Structure

### Classes and Modules

- **Course**
  - Manages course information, including students and modules.
  - Stores all instances in a class variable for easy retrieval.
- **Module**
  - Represents a course module and its associated tutor.
  - Can be loaded from a CSV file.
- **Person**
  - Base class for Student and Tutor with common attributes.
- **Student**
  - Inherits from Person.
  - Represents a student enrolled in a course.
- **Tutor**
  - Inherits from Person.
  - Represents a tutor with a list of subjects they can teach.
- **Room**
  - Represents a generic room with common attributes.
- **ClassRoom**
  - Inherits from Room.
  - Represents a classroom with specific equipment.
- **Gym**
  - Inherits from Room.
  - Represents a gymnasium with specific equipment.
- **Hall**
  - Inherits from Room.
  - Represents a hall with specific equipment.
- **Equipment**
  - Represents equipment details for rooms.
  - Can be loaded from a CSV file.

## Usage

### Creating a Course

```python
from course_files.course import Course

course = Course(course_name="Computer Science", description="A comprehensive course on computer science.")
```

### Adding Students to a Course

```
from person_files.student import Student

student1 = Student(first_name="John", last_name="Doe", student_id=1234567, address="123 Main St", course_name="Computer Science")
course.add_student(student1)
```

### Adding Modules to a Course
```
from course_files.module import Module

module1 = Module(module_name="Introduction to Programming", course_tutor="Jane Smith", course_name="Computer Science")
course.add_module(module1)
```

### Listing All Courses
```
Course.listall()
```

### Loading Data from Files

#### Loading Students from a File
```
students = Student.load_from_file("students.csv")
course.student_list = students
```

#### Loading Modules from a File
```
modules = Module.load_from_file("modules.csv", "tutors.csv")
course.module_list = modules
```

### CSV File Format

#### Students CSV

| first_name | last_name | student_id | address       | course           |
|------------|-----------|------------|---------------|------------------|
| John       | Doe       | 1234567    | 123 Main St   | Computer Science |
| Jane       | Doe       | 7654321    | 456 Main St   | Computer Science |

#### Modules CSV

| course_name       | course_subjects                      |
|-------------------|--------------------------------------|
| Computer Science  | Introduction to Programming, Data Structures |

#### Tutors CSV

| first_name | last_name | address       | role      | subjects                           |
|------------|-----------|---------------|-----------|------------------------------------|
| Jane       | Smith     | 789 Main St   | Professor | Introduction to Programming, Data Structures |
