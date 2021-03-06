# School Management with Python and Sqlite3 database

Create a program that displays the following menu to the user:

Add student
Add course
Add test
Add student to course
List courses by student
List tests by course
Exit

then performs the choice entered by the user. You can reuse code from the previous assignment if you want to.

Data considerations:

Students can take multiple courses and courses contain multiple students (many to many)
Courses can have multiple tests, but a test only belongs to one course (one to many)

All data must be stored in the SQLite database called school.sqlite.

The students table has the following columns:

id integer primary key auto increment
name text
email text
year integer

The courses table has the following columns:

id integer primary key auto increment
name text
max_students integer

The tests table has the following columns:

id integer primary key auto increment
course_id integer foreign key
name text
date_time text

The student_course table is an association table with the following columns:

student_id integer foreign key
course_id integer foreign key

1., 2. and 3.

Asks the user for the table fields in order (without id), then adds the new student/course/test to the database.

Expected output: Added <student/course/test> with id <id>

4.

Asks the user for a student id and a course id then adds the student to the course.

Note: Ask for both ids before checking if they are valid.

Expected output: Added student to course id <id>

Or: Student not found

Or: Course not found

5.

Asks the user for a student id then lists all the courses assigned to this student. The courses must be sorted by id, lowest first.

Expected output: Courses for student <id>: <course name>, <course name> ...

Or: Student not found

6.

Asks the user for a course id then lists all the tests for this course. The tests must be sorted by id, lowest first.

Expected output: Tests for course <id>: <test name>, <test name> ...

Or: Course not found

7. Exit

Exits the program.