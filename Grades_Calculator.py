from prettytable.colortable import ColorTable, Themes
import numpy as np
import json


class Course:
    def __init__(self, name, points, grade, course_type):
        self._name = name
        self._points = points
        self._grade = grade
        self.type = course_type

    def get_name(self):
        return self._name

    def get_points(self):
        return self._points

    def get_grade(self):
        return self._grade

    def get_type(self):
        return self.type


class Student:
    def __init__(self, name, courses):
        self._name = name
        self._courses = [course for course in courses if course.get_type() != "Corner Stone"]
        self._corner_stones = [course for course in courses if course.get_type() == "Corner Stone"]
        self._number_of_courses = len(courses)
        self._total_points = sum([course.get_points() for course in courses])
        self._mean = np.average([course.get_grade() for course in courses],
                                weights=[course.get_points() for course in courses])

    def add_course(self, course):
        if course.get_type() == "Corner Stone":
            self._corner_stones.append(course)
        else:
            self._courses.append(course)
        self._number_of_courses += 1
        self._total_points += course.get_points()
        self._recalculate_mean()

    def remove_course(self, course_name):
        course_to_remove = None
        for course in self._courses + self._corner_stones:
            if course.get_name() == course_name:
                course_to_remove = course
                break
        if course_to_remove:
            if course_to_remove.get_type() == "Corner Stone":
                self._corner_stones.remove(course_to_remove)
            else:
                self._courses.remove(course_to_remove)
            self._number_of_courses -= 1
            self._total_points -= course_to_remove.get_points()
            self._recalculate_mean()

    def update_course(self, course_name, new_course):
        self.remove_course(course_name)
        self.add_course(new_course)

    def _recalculate_mean(self):
        total_courses = self._courses + self._corner_stones
        if total_courses:
            self._mean = np.average([course.get_grade() for course in total_courses],
                                    weights=[course.get_points() for course in total_courses])
        else:
            self._mean = 0

    def print_info(self, sort_by='type', filter_by=None):
        if filter_by:
            courses = [course for course in self._courses if course.get_type() == filter_by]
        else:
            courses = self._courses

        if sort_by == 'name':
            courses.sort(key=lambda x: x.get_name())
        elif sort_by == 'points':
            courses.sort(key=lambda x: x.get_points())
        elif sort_by == 'grade':
            courses.sort(key=lambda x: x.get_grade())
        else:
            courses.sort(key=lambda x: x.get_type())

        fields = ["Course", "Points", "Grade", "Type"]
        table = ColorTable(theme=Themes.OCEAN)
        table.field_names = fields
        for course in courses:
            table.add_row([course.get_name(), course.get_points(),
                           course.get_grade(), course.get_type()])
        print(table)

        if not filter_by:
            corner_stones_table = ColorTable(theme=Themes.OCEAN)
            corner_stones_table.field_names = fields
            for course in self._corner_stones:
                corner_stones_table.add_row([course.get_name(), course.get_points(),
                                             course.get_grade(), course.get_type()])
            print(corner_stones_table)

        print(f"\nYour total number of courses is: {self._number_of_courses}")
        print(f"Your total Points are: {self._total_points}")
        print(f"Your average grade is: {np.round(self._mean, 2)}")

    def get_mean(self):
        return self._mean


def load_courses_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return [Course(course['name'], course['points'], course['grade'], course['type']) for course in data]


def add_course(student):
    name = input("Enter course name: ")
    points = float(input("Enter course points: "))
    grade = float(input("Enter course grade: "))
    course_type = input("Enter course type: ")
    student.add_course(Course(name, points, grade, course_type))


def remove_course(student):
    name = input("Enter course name to remove: ")
    student.remove_course(name)


def update_course(student):
    name = input("Enter course name to update: ")
    new_name = input("Enter new course name: ")
    points = float(input("Enter new course points: "))
    grade = float(input("Enter new course grade: "))
    course_type = input("Enter new course type: ")
    student.update_course(name, Course(new_name, points, grade, course_type))


def display_info(student):
    sort_by = input("Sort by (name, points, grade, type): ")
    filter_by = input("Filter by (type or leave blank): ")
    student.print_info(sort_by, filter_by)


def main():
    Courses_list = [
        # CS Courses:
        Course("Introduction To Computer Science", 7, 82, "CS"),
        Course("Data Structures", 4, 80, "CS"),
        Course("C & C++", 4, 86, "CS"),
        Course("Introduction to OOP", 4, 91, "CS"),
        Course("Computational Models computability and complexity", 5, 68, "CS"),
        Course("Introduction to Cryptography", 4, 87, "CS"),
        Course("Software Engineering", 4, 96, "CS"),
        Course("From Nand To Tetris", 5, 79, "CS"),
        Course("Algorithms", 5, 67, "CS"),
        # Course("Databases", 5, , "CS"),
        # Course("Operating Systems", 4, , "CS"),
        # Course("A Guide for Information Revolutionists", 2, , "CS"),
        # Course("", , , "CS"),
        # Course("", , , "CS"),
        # Course("", , , "CS"),
        # Course("", , , "CS"),
        # Course("Introduction to Machine Learning", 5, , "CS"),

        # Math Courses:
        Course("Infinitesimal Calculus 1", 7, 64, "Math"),
        Course("Infinitesimal Calculus 2", 7, 60, "Math"),
        Course("Linear Algebra 1", 6, 65, "Math"),
        Course("Linear Algebra 2", 6, 84, "Math"),
        Course("Discrete Mathematics", 5, 60, "Math"),
        Course("Probability", 6, 62, "Math"),

        # Earth Courses:
        Course("INTRODUCTION TO CLIMATE", 4, 77, "Earth"),
        Course("THE DYNAMIC EARTH", 4, 90, "Earth"),
        Course("GEOLOGICAL EXCURSION IN THE NEGEV", 1.5, 91, "Earth"),
        # Course("INTRODUCTION TO OCEANOGRAPHY", 3, , "Earth"),
        # Course("", , , "Earth"),
        # Course("", , , "Earth"),
        # Course("", , , "Earth"),
        # Course("", , , "Earth"),
        # Course("", , , "Earth"),
        # Course("", , , "Earth"),
        # Course("", , , "Earth"),
        # Course("", , , "Earth"),

        # Corner Stone Courses:
        Course("Sex With Elephants", 2, 99, "Corner Stone"),
        Course("Design Driven Innovation", 2, 100, "Corner Stone"),
        # Course("Hope: Human Odyssey to Political Existentialism", 2, 100 , "Corner Stone"),
        # Course("Engineer your Entrepreneurship", 2, 98 , "Corner Stone"),
    ]

    student = Student("Noam Shabat", Courses_list)
    while True:
        try:
            command = input("Enter command (add, remove, update, display, exit): ")
            if command == 'add':
                add_course(student)
            elif command == 'remove':
                remove_course(student)
            elif command == 'update':
                update_course(student)
            elif command == 'display':
                display_info(student)
            elif command == 'exit':
                break
            else:
                print("Invalid command.")
        except ValueError as e:
            print(f"Error: {e}")


main()
