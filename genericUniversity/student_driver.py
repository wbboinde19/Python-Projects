class Student():
    def __init__(self,student_object):
        if int(student_object[0]):
            self.ID=int(student_object[0])
        else:
            return "Hey enter an interger or a string that can be converted to an integer"
        if str(student_object[1:5]):
            self.firstName=str(student_object[1])
            self.lastName=str(student_object[2])
            self.email=str(student_object[3])
            self.year=str(student_object[4])
        else:
            return "Hey check your one of our names or your email or year.It must be able to be a string"
        if 0.0<=float(student_object[5])<=4.0:
            self.gpa=float(student_object[5])
        else:
            return "Your GPA is either too small or too big"
    #getters for attributes
    def get_ID(self):
        if self.ID>0:
            return self.ID
        else:
            return "Hey your number ID cannot be negative"
    def get_firstName(self):
        if self.firstName.isalpha():
            return self.firstName
        else:
            return "Your input was not alphabetic"
    def get_lastName(self):
        if self.lastName.isalpha():
            return self.lastName
        else:
            return "Your input was not alphabetic"
    def get_email(self):
        return self.email
    def get_year(self):
        if self.year=="FR" or self.year=="SO" or self.year=="JR" or self.year=="SR":
            return self.year
        else:
            return "Your year has to be FR, SO, JR or SR"
    def get_gpa(self):
        if 0.0<=self.gpa<=4.0:
            return self.gpa
        else:
            return "Invalid GPA"
    #setters for the attributes
    def set_ID(self,to_this):
        self.ID=(to_this)
        if int(self.ID):
            if int(self.ID)>0:
                return self.ID
            else:
                return "Hey set to a positive integer"
        else:
            return "Enter an integer"
    def set_firstName(self,to_this):
        self.firstName=to_this
        if self.firstName.isalpha():
            return self.firstName
        else:
            return "Your input was not alphabetic"
    def set_lastName(self,to_this):
        self.lastName=to_this
        if self.lastName.isalpha():
            return self.lastName
        else:
            return "Your input was not alphabetic"
    def set_email(self,to_this):
        self.email=to_this
        return self.email
    def set_year(self,to_this):
        self.year=to_this
        if self.year=="FR" or self.year=="SO" or self.year=="JR" or self.year=="SR":
            return self.year
        else:
            return "Your year has to be FR, SO, JR or SR"
    def set_gpa(self,to_this):
        if 0.0<=float(to_this)<=4.0:
            self.gpa=float(to_this)
            return self.gpa
        else:
            return "Your GPA is either too small or too big"
def loadStudents(inputFileName):
    inFile=open(inputFileName,"r")
    studentArray=[]
    for line in inFile:
        new_line=""
        for char in line:
            if char!=",":
                new_line+=char
            else:
                new_line+=" "
        studentArray.append(new_line.split())
    inFile.close()
    return studentArray

def displayStudents(studentArray):
    for i in range(len(studentArray)):
            student_object=studentArray[i]
            student_info=Student(student_object)
            new_student_object=""
            new_student_object+=str(student_info.get_ID())+","+student_info.get_firstName()+","+student_info.get_lastName()+","+student_info.get_email()+","+ student_info.get_year()+","+str(student_info.get_gpa())
            print(new_student_object)
def averageGPA(studentArray):
    count=0
    sum=0
    for i in range(len(studentArray)):
        student_object=studentArray[i]
        student_info=Student(student_object)
        gpa=student_info.get_gpa()
        sum+=gpa
        count+=1
    average=round(sum/count,2)
    print(average)
def improveGPA(studentArray,percentImprovement=1.0):
    new_studentArray=[]
    for i in range(len(studentArray)):
        student_object=studentArray[i]
        student_info=Student(student_object)
        gpa=student_info.get_gpa()
        new_gpa=gpa+((percentImprovement/100)*gpa)
        if new_gpa>4.0:
            student_info.set_gpa(4.0)
        else:
            student_info.set_gpa(new_gpa)
        student_object=[student_info.get_ID(),student_info.get_firstName(),student_info.get_lastName(),student_info.get_email(),student_info.get_year(),student_info.get_gpa()]
        new_studentArray.append(student_object)
    studentArray=new_studentArray
    return studentArray

import argparse
if __name__=='__main__':
    parser=argparse.ArgumentParser("input the usage here")
    parser.add_argument("-i",help="input file name",type=str)
    parser.add_argument("-p",help="percent GPA improvement",type=float)
    args=parser.parse_args()
    studentArray=loadStudents(args.i)
    displayStudents(studentArray)
    averageGPA(studentArray)
    studentArray=improveGPA(studentArray,1.0)
    averageGPA(studentArray)
    exit(0)
