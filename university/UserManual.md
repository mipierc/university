
# User Document

## Logging in

---

The user can login using the following link: http://127.0.0.1:8000/accounts/login/ 

This is what the login page will look like to the user.

<img src='images/login.PNG' width=500>

After the user submits their credentials for their account, they will be taken to a homepage where they can choose what action to perfrom next, dependent on their access level.

# Homepage - Admin

---

If the user logs in using an account with admin access level, they will be shown the homepage for the admin.

After logging in the admin level user account, the user has the following options to choose from:
1. Student - actions that a student account can perform
2. Professor - actions that a professor account can perfrom
3. Admin - actions that an admin account can perform
   
The actions that the student and professor account can preform will be explained in their respective sections. The actions that the admin can perform will be detailed in this section.

The admin user account is allowed to access three main functionalities that other accounts cannot access:
1. Admin users can create a list of professors sorted by one of the three criteria:
    * By Name
    * By department
    * By Salary
2. Admin users can create a table of max/average/min salary amounts sorted by department.
    * The user must submit a department name to be given the max/average/min salary information. Else they will be given salary information of every department in the database.
3. Admin users can create a table of a professor's name, department, and number of student taught by the professor in a given semester.
    * The user must input semester ("1" for Spring and "2" for Fall) and the year they wish to access.

## The admin actions' page view
<img src='images/admin.PNG' width=500>

## The following are example outputs using the different actions allowed to the admin user account:

### Example 1: List of professors sorted by name:

<img src='images/aex1.PNG' width=500>

### Example 2: Salary information for 'CS':

<img src='images/aex2.PNG' width=500>

### Example 3: Students taught by a professor for 'Spring 2019':

<img src='images/aex3.PNG' width=500>

# Homepage - Professor

---

If the user logs in using an account with professor access level, they will be shown the homepage for the professor.

After logging in the professor level user account, the user has the following options to choose from:
1. Student - actions that a student account can perform
2. Professor - actions that a professor account can perfrom

The actions that the student account can preform will be explained in its' respective section. The actions that the professor can perform will be detailed in this section.

The professor user account is allowed to access 2 main functionalities that other accounts cannot, besides admin:
1. Professor users can create a list of course sections and number of students enrolled in each section that the professor has taught in a given semester.
    * The user must input a course and section id in order to view the courses. If no input is provided, the user is shown information about each course.
2. Professor users can create a list of students enrolled in a course section taught by a professor in a given semester.
    * The user must input a professor's name, semester ("1" for Spring and "2" for Fall), and year to view that specific course's students. Else, if no information is provided, all the students with what course they are enrolled in.

## The professor action's page view:
<img src='images/professor.PNG' width=700>

## The following are example outputs using the different actions allowed to the professor user account:

### Example 1: Results for CS141 Section 1
<img src='images/pex1.PNG' width=700>

### Example 2: Results for Professor Hou in semester 1 of 2020
<img src='images/pex2.PNG' width=700>

## Homepage - Student

---

If the user logs in using an account with professor access level, they will be shown the homepage for the professor.

The student user account is allowed to access 1 main functionality:
1. Student users can create a list of course sections offered by department in a given semester and year.
    * The user must input the department, semester ("1" for Spring and "2" for Fall), and year to view results. Else, all courses are shown with their respective semesters and years.

## The student action's page view:
<img src='images/student.PNG' width=700>

## The following are example output using the different actions allowed to the student user account:

### Example 1: Results for CS department for CS141 of Fall 2019:
<img src='images/sex1.PNG' width=700>

## Logging Out & Home

---

Under each homepage there is an option to log out of the account. There is also an option to log out on the action page for each account level. On the account action page, there is a page to go home, where it will redirect the user back to the home page.