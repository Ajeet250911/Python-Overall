class Student:
    CourseName="Python" #class variable
    InstName="Precursor"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getdetails(self):
        print("Name of the student is "+self.name)
        print("Student age is",self.age)
        print("Course name for the student is "+Student.CourseName)
        print("Institute name for the student is "+Student.InstName)

print("Course and Institute name is "+Student.CourseName+" and "+Student.InstName+" respectively.") #without object
s=Student("Scott",20)
s.getdetails()

##**Use of Builtin class variable**##
print(Student.__dict__)
print(Student.__name__)
print(Student.__module__)
print(Student.__bases__)
print(Student.__doc__)