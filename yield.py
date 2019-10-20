students = []

def read_file():
    try:
        file = open("students.txt", "r")
        for student in read_students(file):
            students.append(student)
        file.close()
    except Exception:
        print("Could not read file")


def read_students(file):
    for line in file:
        yield line


read_file()
print(students)
