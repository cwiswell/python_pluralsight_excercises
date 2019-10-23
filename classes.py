students = []


class Student:

    school_name = "Georgia Institute of Technology"

    def __init__(self, name, student_id=42):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return f"Student {self.name}"

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):

    school_name = "Perry High School"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return f"{original_value} - HS"


jason = HighSchoolStudent('jason')

print(jason.get_name_capitalize())


bob = Student("Bob")

print(bob)
print(students)

print(Student.school_name)
