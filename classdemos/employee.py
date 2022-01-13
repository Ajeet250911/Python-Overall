class Employee:
    def setinfo(self,name,id,salary):   #instance method ->self represents current obj
        self.name=name   #self.variable name ->instance variable
        self.id=id
        self.salary=salary  #instance variable is global variable ,can be used in any method of the particular class

    def printinfo(self):
        print("Employee name is",self.name)
        print("Employee id is", self.id)
        print("Employee salary is", self.salary)

    def __str__(self):
        return "this is employee class "+self.name

emp=Employee() #emp is the object of the Employee class
emp.setinfo("Scott",101,50000.00)
emp.printinfo()

name=input("Enter name")
id=input("Enter id")
salary=input("Enter salary")
emp1=Employee()
emp1.setinfo(name,id,salary)
emp1.printinfo()

print(emp)
print(emp1)

print(issubclass(Employee,object)) #proving superclass is inherited with a superclass object