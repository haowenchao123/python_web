from orm import session, Student, Class

sStudents = session.query(Student).join(Class).filter(Class.level == 3).all()
for student in sStudents:
    print(student.name)

for student, class_ in session.query(Student, Class).join(Class).filter(Class.level==3).all():
	print(student.name, class_.name)

for student_name, in session.query(Student.name).join(Class, Class.address == Student.address).filter(Class.level == 3).all():
	print(student_name)


		