students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


userAnswer = input("Would you like to enter a student? ")
while userAnswer == "yes":
    student_name = input("Enter students name: ")
    student_id = input("Enter student Id:")

    add_student(student_name, student_id)
    userAnswer = input("Would you like to continue entering students? ")

print_students_titlecase()
