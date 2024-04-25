# Generic University
Contains three python files. `student_driver.py`, `university_driver.py`, and `ec_driver.py`. 

## Student Driver
### Tasks
Developed a class named Student with the following attributes and methods:
1. ID: stores the unique ID number of a student.
2. firstName: stores the first name of a student.
3. lastName: stores the last name of a student.
4. email: stores the email address of a student.
5. year: stores which year (FR, SO, JR, SR) the student is in.
6. gpa: stores student’s GPA in float. ( 0.0 ≤ GPA ≤ 4.0 )
7. Getters and setters: getters and setters for each of the class attributes. (get_email, etc.)

Inputs are validated and error messages are printed under invalid conditions; no exceptions raised.

Wrote a function loadStudents(inputFileName) that takes the input file name as an argument and
returns an array of populated Student objects. This was done by iterating over the input file, and
for each line instantiating & populating a Student object. Each line holds information for one student
object. I Store all the objects in an array which is returned as the array of student objects.

Wrote a function displayStudents(studentArray) that takes an array of Student objects and uses
the getters to print their contents to stdout (standard output) in CSV (comma-separated values)
format, like so:
`ID, firstName, lastName, email, year, gpa`
`...`

Wrote a function averageGPA(studentArray) that takes an array of Student objects and uses the
getters to calculate and print their collective average GPA rounded to 2 decimal places to stdout.

Wrote a function improveGPA(studentArray, percentImprovement = 1.0) that traverses an array
of Student objects and uses the appropriate methods to increase every student’s GPA by the amount
of the float variable percentImprovement that is given as a parameter in the function description.
(Note that GPAs cannot be greater than 4.0; if the calculated GPA is > 4.0, set it to 4.) The default
value for improvement is 1.0% as defined in the function description above.

In the main() function, I process the command line arguments. The input file name and the percent
GPA improvement are required command line arguments (-i and -p). I also invoke my functions in this exact order: loadStudents(),
displayStudents(), averageGPA(), improveGPA(), and averageGPA(). 

From the command line, I redirect the output into a file named studentsWGPA.csv. The output file contains the list of students with the two average GPAs at the end.

### Implementation Notes
1. The input file name and the percent GPA improvement should be required command line
arguments (-i and -p)
2. Checks to make sure the file exists before calling loadStudents(inputFileName)
3. A sample CSV input file, and expected canon, are available.

## University Driver
### Setup
`university_driver.py` has two different types of students, undergraduate, and graduate, with these attributes we would like to track:
* All students have a studentType (e.g. under, grad), first name, last name, ID number, email
* Undergraduate students also have a dormRoom (e.g. BUNDY201)
* Graduate students also have an office (e.g. CST218)

university_driver offers courses with the following attributes and enrollment rules:
* Courses have a department (e.g. CS) and a number (e.g. 256)
* enrolledIDList, a list of student IDs that have been properly enrolled in the class

### Tasks
1. Designed a family of classes, one for each type of student plus a base class, that include all of the data elements listed above.
2. Designed a course class that includes all the data elements listed above. It also provides `enrollStudent(studentID)`, and a `countStudents()` method that returns the number of students in the class. 
3. Wrote a function `loadStudents(inputFileName)` that takes a student input file name as an argument and returns an array of populated Student objects.
4. Wrote a function `enrolling(inputFileName, studentArray)` that takes a course enrollment input file name and a list of all student objects as arguments and returns a populated course object for CS256 (the data file is assumed to have entries only for CS256). This is done by instantiating the course object and then iterating over the input and for each line checking the validity of the ID and then calling the courseObject.enrollStudent() method.
5. My main() processed the command line arguments and then invokes my functions in this order: loadStudents(), enrolling(), cs256CourseObject.countStudents(), and some print() statements. It also has the list of student objects as in `student_driver.py`. 

From the command line the output file is redirected into a file named `enrollmentCounts.csv`.

### Implementation Notes
1. Worked-out the complete design on paper.
2. The student input file name and the course enrollment input file name are required command line arguments (-s and -e).
4. Checks to make sure the appropriate file exists before calling `loadStudents()` and `enrolling()`.
5. CSV formatted data files of students and enrollments are available for use in testing
    * `allStudents.csv`
        > studentType, studentID, lastName, firstName, email, <aPlace>
        
        >                           ...
    * `cs256Enrollments.csv`
        > studentID
        
        >       ...

## EC driver
`ec_driver.py` is same as university driver but contains one more command line argument: **-d <file>**. `dropStudent(studentID)` method and a `dropStudents(inputFileName, courseObject)` function are implemented too. `dropStudent(studentID)` removes the input student ID from the list of enrolled students in that course. `dropStudents(inputFileName, courseObject)` drops all students in the input file by iterating over the input file and then calling the `dropStudent()` method.