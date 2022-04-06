from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
import mysql.connector

def index(request):
    return HttpResponse("Welcome to the University Database.\nPlease log in:")

def student(request):
    db = mysql.connector.connect(
            host = "128.153.190.69",
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

def professor(request):
        db = mysql.connector.connect(
            host = "128.153.190.69",
            user = "root",
            passwd = "password",
            auth_plugin = "mysql_native_password",
            database = "university",
            )
        
        cursor = db.cursor()
        cursor.execute("select name, dept_name, salary from instructor;")

        data='<title>Instructor Info</title>'
        data='<h1>Instructors:</h1>'
        data += '<table style="width:800px">'
        data += '<tr><th>Instructor Name</th> <th>Department Name</th>' + \
                '<th>Salary</th>'
       
        for(name, dept_name, salary) in cursor:
           r = ('<tr>' + \
                '<th>' + str(name) + '</th>' + \
                '<th>' + dept_name + '</th>' + \
                '<th>' + str(salary) + '</th>' + \
                '</t>')
           data += r
        data += '</table>'

        cursor.close()
        db.close()

        return HttpResponse(data)

