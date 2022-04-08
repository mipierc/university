from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
import mysql.connector
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Welcome to the University Database.\nPlease log in:")

def student(request):
    db = mysql.connector.connect(
            host = "128.153.174.218",
            user = "root",
            passwd = "password",
            auth_plugin = "mysql_native_password",
            database = "university",
        )

    cursor = db.cursor()

    department = request.POST['department']
    semester = request.POST['semester']
    year = request.POST['year']
    query = "select course.course_id, title, dept_name, sec_id, semester, year from course natural join section " + \
            "where course.course_id=section.course_id"
    if department != "":
        query += " and dept_name=\"" + department + "\""
    if semester != "":
        query += " and semester=\"" + semester + "\""
    if year != "":
        query += " and year=\"" + year + "\""
    query += ";"
    cursor.execute(query)

    data='<title>Student Info</title>'
    data='<h1>Courses:</h1>'
    data += '<table style="width:800px">'
    data += '<tr><th>Course ID</th> <th>Course Title</th>' + \
            '<th>Department Name</th> <th>Section</th>' + \
            '<th>Semester</th> <th>Year</th></tr>'
    for (course_id, sec_id, title, dept_name, semester, year) in cursor:
        r = ('<tr>' + \
                '<th>' + str(course_id) + '</th>' + \
                '<th>' + str(sec_id) + '</th>' + \
                '<th>' + title + '</th>' + \
                '<th>' + dept_name + '</th>' + \
                '<th>' + str(semester) + '</th>' + \
                '<th>' + str(year) + '</th>' + \
                '</t>')
        data += r
    data += '</table>'
   
    cursor.close()
    db.close()

    return HttpResponse(data)

def administrator(request):

    form = '<!DOCTYPE html>' + \
        '<html>' + \
        '<body>' + \
        '<h1>Administrator:</h1>' + \
        '<h3> Choose which following Functions to perform: </h3>' + \
        '<form action="f1/" method="post">' + \
            '<p> F1. Create a list of professors sorted by: <p>' + \
            '<INPUT TYPE=radio NAME="sort_method" VALUE="name" CHECKED> Name</LABEL><BR>' + \
            '<INPUT TYPE=radio NAME="sort_method" VALUE="dept"> Department</LABEL><BR>' + \
            '<INPUT TYPE=radio NAME="sort_method" VALUE="salary"> Salary</LABEL>' + \
            '<p> </p>' + \
            '<input type="submit" value = "View professors">' + \
        '</form><br><br>' + \
        '<form action="f2/" method="post">' + \
            '<p> F2. Create a table of the min/max/average salaries of a department: <p>' + \
            '<input type-"text" id="department" name="department"><br><br>' + \
            '<input type="submit" value = "View salaries">' + \
        '</form><br><br>' + \
        '<form action="f3/" method="post">' + \
            '<p> F3. Create a table of professors, their department and how many students they taught in a given semester: <p>' + \
            '<input type-"text" id="semester" name="semester"><br><br>' + \
            '<input type="submit" value = "View professors">' + \
        '</form>' + \
        '<p>Choose a function above.</p>' + \
        '<p><a href="/">Home</a></p>' + \
        '<p><a href="/accounts/login/">Log Out</a></p>' + \
        '</body>' + \
        '</html>'

    return HttpResponse(form)

@csrf_exempt
def f1(request):
    db = mysql.connector.connect(
        host = "128.153.174.218",
        user = "root",
        passwd = "password",
        auth_plugin = "mysql_native_password",
        database = "university",
    )

    cursor = db.cursor()
    cursor.execute("select ;")

    sort_method = request.POST['sort_method']
    query = "select * from instructor order by " + sort_method + ";"
    cursor.execute(query)

    data='<title>Administrator Info</title>'
    data='<h1>Results:</h1>'
    data += '<table style="width:400px">'
    data += '<tr><th>ID</th> <th>Name</th> <th>Dept</th> <th>Salary</th> </tr>'
    for (ID, name, dept, salary) in cursor:
        r = ('<tr>' + \
                '<th>' + str(ID) + '</th>' + \
                '<th>' + str(name) + '</th>' + \
                '<th>' + str(dept) + '</th>' + \
                '<th>' + str(salary) + '</th>' + \
                '</t>')
        data += r
    data += '</table>'
    data += '<a href="/admin/">Back</a>'

    cursor.close()
    db.close()

    return HttpResponse(data)

@csrf_exempt
def f2(request):
    db = mysql.connector.connect(
        host = "128.153.174.218",
        user = "root",
        passwd = "password",
        auth_plugin = "mysql_native_password",
        database = "university",
    )  

    cursor = db.cursor()
    dept = request.POST['department']
    query = "select MAX(salary), MIN(salary), AVG(salary) from instructor where instructor.dept_name = " + dept + ";"
    cursor.execute(query)

    data='<title>Administrator Info</title>'
    data='<h1>Results:</h1>'
    data += '<table style="width:400px">'
    data += '<tr><th>Max</th> <th>Min</th> <th>Average</th></tr>'
    for (max, min, avg) in cursor:
        r = ('<tr>' + \
                '<th>' + str(max) + '</th>' + \
                '<th>' + str(min) + '</th>' + \
                '<th>' + str(avg) + '</th>' + \
                '</t>')
        data += r
    data += '</table>'
    data += '<a href="/admin/">Back</a>'

    cursor.close()
    db.close()

    return HttpResponse(data)

@csrf_exempt
def f3(request):
    db = mysql.connector.connect(
        host = "128.153.174.218",
        user = "root",
        passwd = "password",
        auth_plugin = "mysql_native_password",
        database = "university",
    )

    cursor = db.cursor()
    semester = request.POST['semester']
    query = "select instructor.name, instructor.dept_name, COUNT(student.name) from instructor, student, teaches, takes where instructor.ID = teaches.ID AND teaches.course_id = takes.course_id AND takes.ID = student.ID "
    if semester != "":
        query += "and takes.semester = " + semester + ";"
    cursor.execute(query)

    data='<title>Administrator Info</title>'
    data='<h1>Results:</h1>'
    data += '<table style="width:400px">'
    data += '<tr><th>Name</th> <th>Dept</th> <th>Number of Students</th> </tr>'
    for (name, dept, count) in cursor:
        r = ('<tr>' + \
                '<th>' + str(name) + '</th>' + \
                '<th>' + str(dept) + '</th>' + \
                '<th>' + str(count) + '</th>' + \
                '</t>')
        data += r
    data += '</table>'
    data += '<a href="/admin/">Back</a>'

    cursor.close()
    db.close()

    return HttpResponse(data)
    
def professor(request):
    form = '<!DOCTYPE html>' + \
        '<html>' + \
        '<body>' + \
        '<h1>Professor:</h1>' + \
        '<form action="courses/" method="post">' + \
            '<input type-"text" id="ID" name="ID">' + \
            '<label for="ID"> Teacher ID</label><br>' + \
            '<input type-"text" id="semester" name="semester">' + \
            '<label for="semester"> Semester [1 for fall, 2 for spring]</label><br>' + \
            '<input type-"text" id="year" name="year">' + \
            '<label for="year"> Year [XXXX]</label><br>' + \
            '<input type="submit" value = "View courses">' + \
        '</form><br><br>' + \
        '<form action="students/" method="post">' + \
            '<input type-"text" id="courseID" name="courseID">' + \
            '<label for="courseID"> Course ID</label><br>' + \
            '<input type-"text" id="semester" name="semester">' + \
            '<label for="semester"> Semester [1 for fall, 2 for spring]</label><br>' + \
            '<input type-"text" id="year" name="year">' + \
            '<label for="year"> Year [XXXX]</label><br>' + \
            '<input type="submit" value="View students">' + \
        '</form>' + \
        '<p>Choose what to do.</p>' + \
        '</body>' + \
        '</html>'

    return HttpResponse(form)

@csrf_exempt
def professorCourses(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        auth_plugin="mysql_native_password",
        database="university",
    )

    mycursor = mydb.cursor()

    lastName = request.POST['ID']
    semester = request.POST['semester']
    year = request.POST['year']
    query = "select C.course_id as course_id, count(C.course_id) as count from (select course.course_id, takes.id" + \
            " from course join takes where course.course_id=takes.course_id) C group by C.course_id;"
    mycursor.execute(query)

    data = '<h1>Courses:</h1>'
    data += '<table style="width:800px">'
    data += '<tr><th>Course ID</th> <th>Number of Students</th></tr>'
    for (course_id, count) in mycursor:
        r = ('<tr>' +
             '<th>' + str(course_id) + '</th>' +
             '<th>' + str(count) + '</th>' +
             '</t>')
        data += r
    data += '</table>'
    data += '<a href="">Go back</a>'
    mycursor.close()
    mydb.close()

    return HttpResponse(data)

@csrf_exempt
def professorStudents(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        auth_plugin="mysql_native_password",
        database="university",
    )

    mycursor = mydb.cursor()

    department = request.POST['courseID']
    semester = request.POST['semester']
    year = request.POST['year']
    return HttpResponse("Professor: View students")