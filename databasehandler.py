import sqlite3

conn = sqlite3.connect('school.sqlite')
curr = conn.cursor()

def create_tables():
    create_tables_query = '''
    CREATE TABLE IF NOT EXISTS "students" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "name"	TEXT,
        "email"	TEXT,
        "year"	INTEGER
    );
    CREATE TABLE IF NOT EXISTS "courses" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "name"	TEXT,
        "max_students"	INTEGER
    );
    CREATE TABLE IF NOT EXISTS "tests" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "course_id"	INTEGER,
        "name" TEXT,
        "date_time" TEXT,
        FOREIGN KEY("course_id") REFERENCES courses(id)
    );
    CREATE TABLE IF NOT EXISTS "student_course" (
        "student_id" INTEGER,
        "course_id" INTEGER,
        FOREIGN KEY("course_id") REFERENCES courses(id)
        FOREIGN KEY("student_id") REFERENCES students(id)
    )
    '''

    curr.executescript(create_tables_query)

def executeCommands(queries):
    curr.execute(queries)
    conn.commit()
    return curr.lastrowid

def addStdCourse(std_id, course_id):
    curr.execute('SELECT id FROM students where id = (?)', std_id)
    rowsSt = curr.fetchall()

    curr.execute('SELECT id FROM courses where id = (?)', course_id)
    rowsCrs = curr.fetchall()

    if len(rowsSt) == 0 or len(rowsCrs) == 0:
        return 0

    else:
        curr.execute('''insert into student_course VALUES (?,?)''', (std_id, course_id))
        conn.commit()
        return 1

def listCourse(st_id):
    st = 1
    curr.execute("SELECT id FROM students WHERE id='" + st_id + "'")
    rowsSt = curr.fetchall()

    if len(rowsSt) == 0:
        st = 0

    curr.execute("SELECT courses.name FROM courses, students, student_course WHERE students.id = student_course.student_id AND courses.id = student_course.course_id AND students.id = '"+ st_id + "'")
    courses = curr.fetchall()

    return st, courses

def getTestsFromCourse(course_id):
    course = 1
    curr.execute("SELECT id FROM courses WHERE id='" + course_id + "'")
    rowsCr = curr.fetchall()

    if len(rowsCr) == 0:
        course = 0

    curr.execute("SELECT name FROM tests WHERE course_id='" + course_id + "'")
    tests = curr.fetchall()

    return course, tests


def addTest():
    print("Enter Course ID : ", end="")
    course_id = input()
    print("Enter Test Name : ", end="")
    test_name = input()
    print("Enter Date : ", end="")
    test_date = input()

    curr.execute("SELECT id FROM courses WHERE id='" + course_id + "'")
    rowsCr = curr.fetchall()

    if len(rowsCr)>0:
        queries = "INSERT INTO tests (course_id, name, date_time) VALUES (" + "'" + course_id + "'" + "," + "'" + test_name + "'" + "," + test_date + ")"
        id = executeCommands(queries)

        # printing tests
        print("Test added with id " + str(id))
        print("\n")
    else:
        print("Course ID not found!")
        print("\n")