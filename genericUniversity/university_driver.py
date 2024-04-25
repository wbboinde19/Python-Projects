class Student():
    def __init__(self,student_object): # student_object contains a list of student information.
        self._student_type=student_object[0]
        self._firstName=student_object[3]
        self._lastName=student_object[2]
        self._ID_number=student_object[1]
        self._email=student_object[4]
    # writing getters
    def get_student_type(self):
        return self._student_type
    def get_firstName(self):
        return self._firstName
    def get_lastName(self):
        return self._lastName
    def get_ID_number(self):
        return self._ID_number
    def get_email(self):
        return self._email
# The setters of the Student base class.
    def set_student_type(self,set):
        self._student_type=set
    def set_firstName(self,set):
        self._firstName=set
    def set_lastName(self,set):
        self._lastName=set
    def set_ID_number(self,set):
        self._ID_number=set
    def set_email(self,set):
        self._email=set

    def Display(self):# this method will display a list of student information.
        return [self.get_student_type(),self.get_ID_number(), self.get_lastName(),self.get_firstName(),self.get_email()]

class Undergraduate(Student):
    def __init__(self,student_object,dormRoom):
        super().__init__(student_object)
        self._dormRoom=dormRoom
    def get_dormRoom(self):
        return self._dormRoom
    def set_dormRoom(self,set):
        self._dormRoom=set

    def displayU(self):
        student_obj=self.Display()
        student_obj.append(self.get_dormRoom())
        return student_obj

class Graduate(Student):
    def __init__(self,student_object,Office):
        super().__init__(student_object)
        self._Office=Office
    def get_Office(self):
        return self._Office
    def set_Office(self,set):
        self._Office=set

    def displayG(self):
        student_obj=self.Display()
        student_obj.append(self.get_Office())
        return student_obj


class Courses():
    def __init__(self,department,number):
        self._department=department
        self._number=number
        self._enrollIDList=[]

    def get_department(self):
        return self._department

    def get_number(self):
        return self._number

    def get_enrollIDList(self):
        return self._enrollIDList

    def set_department(self,set):
        self._department=set

    def enrollStudent(self,StudentID):
        self._enrollIDList.append(StudentID)

    def CountStudents(self):
        list=self.get_enrollIDList()
        count=len(list)
        return count


def loadStudents(inputFileName): # inputFileName is a file of allStudents
    inFile=open(inputFileName,"r")
    studentArray=[] # An empty list for storing the student_objects
    for line in inFile:
        new_line=line.split(",") # creates a student_object out of each line
        orgn=Student(new_line[0:5])# Instantiates the Student class
        student_type=orgn.get_student_type() # Gets the student_type from the the Student class
        if student_type=="under": # IF the student_type is Undergraduate
            Ustudent=Undergraduate(orgn.Display(),student_type) # instantiate the Undergraduate class
            studentArray.append(Ustudent.displayU()) # appends the Undergraduate student object to the studentArray
        if student_type=="grad": # If the student is a Graduate it should do same as above
            Gstudent=Graduate(orgn.Display(),student_type)
            studentArray.append(Gstudent.displayG())
    inFile.close()
    return studentArray

def enrolling(inputFileName,studentArray): # inputFileName contains the IDs of students.
    inFile=open(inputFileName,"r")
    IDlist=inFile.read().split("\n") # creates a lise of IDs
    cs256CourseObject=Courses("CS",256)
    courseObject=[]
    for a in range(len(IDlist)):
        ID=IDlist[a]
        for i in range(len(studentArray)):
            student_object=studentArray[i]
            if ID==student_object[1]: # IF the ID in the file exists in the StudentArray
                cs256CourseObject.enrollStudent(ID) # we enroll the student
                courseObject.append(student_object)
    inFile.close()
    return cs256CourseObject # we return the class

import argparse
if __name__=='__main__':
    parser=argparse.ArgumentParser("Usage")
    parser.add_argument("-s",help="student input File",type=str)
    parser.add_argument("-e",help="course enrollment input File",type=str)
    parser.add_argument("-d",help="file",type=str)
    args=parser.parse_args()
    studentArray=loadStudents(args.s)
    cs256CourseObject=enrolling(args.e,studentArray)
    print(cs256CourseObject.CountStudents())
