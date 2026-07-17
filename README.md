# Student Result Management System
A console-based Python application to manage student academic records--built with core Python,file handling, and JSON for data storage

## Features
-Add new student records(roll number,name, marks in 3 subjects)
-Automatically calculates total,average,and grade
-View all student records
-Search for a student by roll number
-Delete a student record
-Data is saved persistently in a JSON file(students.json)

## Technologies Used
-Python 3
-JSON (for data persistence)
-pathlib (for file handling)

## How to Run
1.Make sure Python 3 is installed
2.Run the script:
  python student_result_management_system.py
3.Follow the on-screen menu to add, view, search, or delete student reords

## Grading Logic
|Average|Grade|
|-------|-----|
|90+    | A+  |
|80-89  | A   |
|70-79  | B   |
|60-69  | C   |
|50-59  | D   |
|Below 50| F  |

## Author
Amaya