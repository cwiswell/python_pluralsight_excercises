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


def save_file(student):
    try:
        file = open("students.txt", "a")
        file.write(student + "\n")
        file.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        file = open("students.txt", "r")
        for student in file.readlines():
            add_student(student)
        file.close()
    except Exception:
        print("Could not read file")


read_file()
print_students_titlecase()

student_name = input("Enter students name: ")
student_id = input("Enter student Id:")

save_file(student_name)

# userAnswer = input("Would you like to enter a student? ")
# while userAnswer == "yes":
#     student_name = input("Enter students name: ")
#     student_id = input("Enter student Id:")
#
#     add_student(student_name, student_id)
#     userAnswer = input("Would you like to continue entering students? ")
#
# print_students_titlecase()
