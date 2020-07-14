import databasehandler as db


def addStudent():
	print("Enter Student Name : ", end = "")
	st_name = input()
	print("Enter Email : ", end="")
	st_email = input()
	print("Enter Year : ", end="")
	st_year = input()
	queries = "INSERT INTO students (name, email, year) VALUES (" + "'" + st_name + "'" + "," + "'" + st_email + "'" + "," + st_year + ")"
	id = db.executeCommands(queries)
	print("Student added with id " +str(id))
	print("\n")

def addCourse():
	print("Enter Course Name : ", end="")
	course_name = input()
	print("Enter Maximum Student : ", end="")
	max_st = input()
	queries = "INSERT INTO courses (name, max_students) VALUES (" + "'" + course_name + "'" + "," + max_st + ")"
	id = db.executeCommands(queries)
	print("Course added with id " + str(id))
	print("\n")

def addStudentToCourse():
	print("Enter Student ID : ", end = "")
	st_id = input()
	print("Enter Course ID : ", end="")
	course_id = input()
	ret = db.addStdCourse(st_id, course_id)

	if ret:
		print("Added student to course id " + course_id)
		print("\n")
	else:
		print("Student or course id not found!")
		print("\n")

def listCourseByStudent():
	print("Enter student id : ", end = "")
	st_id = input()
	st, courses = db.listCourse(st_id)

	cr = []

	## convert this list of tuple to list
	for c in courses:
		cr.append(c[0])

	if st:
		print("Courses for student " + st_id + ": ", end='')
		if len(courses) > 0:
			for course in cr:
				print(course, end=", ")
		print("\n")
	else:
		print("Student id not found")
		print("\n")


def listTestByCourse():
	print("Enter Course Id : ", end = "")
	course_id = input()
	cr, tests = db.getTestsFromCourse(course_id)

	ts = []

	## convert this list of tuple to list
	for t in tests:
		ts.append(t[0])

	if cr:
		print("Tests for course " + course_id + ": ", end='')
		if len(tests) > 0:
			for test in ts:
				print(test, end=", ")
		print("\n")
	else:
		print("Course id not found")
		print("\n")


print("-----------Welcome to School!------------ \n")

#create tables
db.create_tables()

while True:
	menuitems = ["Add student", "Add course", "Add test", "Add student to course",
				 "List courses by student", "List tests by course", "Exit"]

	i = 1
	for item in menuitems:
		print(str(i) + ". " + item)
		i += 1

	menunumber = int(input("Enter menu number : "))

	if menunumber == 1:
		addStudent()
	elif menunumber == 2:
		addCourse()
	elif menunumber == 3:
		db.addTest()
	elif menunumber == 4:
		addStudentToCourse()
	elif menunumber == 5:
		listCourseByStudent()
	elif menunumber == 6:
		listTestByCourse()
	elif menunumber == 7:
		exit()
	else:
		print("Unknown command!")
