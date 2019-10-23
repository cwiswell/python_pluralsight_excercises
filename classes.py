students = []


class Student:
    def __init__(self, name, student_id=42):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student"

    def get_name_capitalize(self):
        return self.name.capitalize()


bob = Student("Bob")

print(bob)
print(students)
