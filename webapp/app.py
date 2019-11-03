from flask import Flask, render_template, redirect, url_for, request

from student import Student

students = []

app = Flask(__name__)


@app.route("/", methods=["GET"])
def students_page():
    return render_template("index.html", students=students)


@app.route("/", methods=["POST"])
def add_student():
    process_add_request(request.form)

    return redirect(url_for("students_page"))


def process_add_request(form):
    new_student_id = form.get("student-id", "")
    new_student_name = form.get("name", "")
    new_student_last_name = form.get("last-name", "")

    new_student = Student(name=new_student_name, last_name=new_student_last_name, student_id=new_student_id)
    students.append(new_student)

# need to run in CMD: set FLASK_APP=app.py
# set in CMD: FLASK_ENV=development
# then run: python -m flask run
