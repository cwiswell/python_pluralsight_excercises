class Student:

    school_name = "Georgia Institute of Technology"

    def __init__(self, name, student_id=42):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Student {self.name}"

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
