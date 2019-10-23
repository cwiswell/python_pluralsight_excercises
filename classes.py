students = []


class Student:

    school_name = "Georgia Institute of Technology"

    def __init__(self, name, student_id=42):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


bob = Student("Bob")

print(bob)
print(students)

print(Student.school_name)
