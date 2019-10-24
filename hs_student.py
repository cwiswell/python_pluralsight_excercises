from student import *


class HighSchoolStudent(Student):

    school_name = "Perry High School"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return f"{original_value} - HS"
