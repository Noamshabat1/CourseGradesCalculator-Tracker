# CourseGradesCalculator-Tracker

An interactive Python application designed to manage student courses, calculate average grades, and display course information. Features include adding, removing, updating, and sorting courses with an intuitive command-line interface.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Add Courses**: Easily add new courses with name, points, grade, and type.
- **Remove Courses**: Remove courses by name.
- **Update Courses**: Update the details of existing courses.
- **Display Information**: View a sorted and filtered list of courses with detailed information.
- **Calculate Averages**: Automatically calculate the average grade based on course points and grades.

## Installation
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/Noamshabat1/CourseGradesCalculator-Tracker.git
    cd CourseGradesCalculator-Tracker
    ```
2. **Create and Activate Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```
3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
Run the application with:
```sh
python Grades_Calculator.py
```
Follow the on-screen prompts to interact with the application.

## Commands
- **Add Course**: Add a new course by providing its details.
- **Remove Course**: Remove an existing course by its name.
- **Update Course**: Update the details of an existing course.
- **Display Info**: Display sorted and/or filtered course information.
- **Exit**: Exit the application.

## Example
```sh
Enter command (add, remove, update, display, exit): add
Enter course name: Introduction to AI
Enter course points: 5
Enter course grade: 90
Enter course type: CS
Course added successfully.

Enter command (add, remove, update, display, exit): display
Sort by (name, points, grade, type): grade
Filter by (type or leave blank): CS
+----------------------+--------+-------+------+
|        Course        | Points | Grade | Type |
+----------------------+--------+-------+------+
|Software Engineering  |   4    |  96   |  CS  |
|Cryptography          |   4    |  87   |  CS  |
|Introduction to AI    |   5    |  90   |  CS  |
+----------------------+--------+-------+------+
Your total number of courses is: 10
Your total Points are: 50
Your average grade is: 85.4
```

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests for any enhancements, bug fixes, or new features.

1. **Fork the Repository**
2. **Create a Feature Branch** (\`git checkout -b feature/NewFeature\`)
3. **Commit Your Changes** (\`git commit -m 'Add new feature'\`)
4. **Push to the Branch** (\`git push origin feature/NewFeature\`)
5. **Open a Pull Request**

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Developed with ❤️ by [Noam Shabat](https://github.com/Noamshabat1)
