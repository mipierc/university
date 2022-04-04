from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
import mysql.connector

def index(request):
    return HttpResponse("Welcome to the University Database.\nPlease log in:")

def student(request):
    db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "password",
            auth_plugin = "mysql_native_password",
            database = "university",
            )

    cursor = db.cursor()
    cursor.execute("select course.course_id, title, dept_name, sec_id, semester, year from course join teaches where course.course_id=teaches.course_id;")

    data='<title>Student Info</title>'
    data='<h1>Courses:</h1>'
    data += '<table style="width:800px">'
    data += '<tr><th>Course ID</th> <th>Course Title</th>' + \
            '<th>Department Name</th> <th>Section</th>' + \
            '<th>Semester</th> <th>Year</th></tr>'
    for (course_id, sec_id, title, dept_name, semester, year) in cursor:
        r = ('<tr>' + \
                '<th>' + str(course_id) + '</th>' + \
                '<th>' + title + '</th>' + \
                '<th>' + dept_name + '</th>' + \
                '<th>' + str(sec_id) + '</th>' + \
                '<th>' + str(semester) + '</th>' + \
                '<th>' + str(year) + '</th>' + \
                '</t>')
        data += r
    data += '</table>'

    cursor.close()
    db.close()

    return HttpResponse(data)