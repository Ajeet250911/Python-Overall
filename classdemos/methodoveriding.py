class Person:
    def setdetails(self,name,age):
        self.name=name
        self.age=age
    def getdetails(self):
        print("Person name is",self.name,"and",self.name,"is",self.age,"years old")

class Employee(Person):
    def setinfo(self,cname,id):
        self.cname=cname
        self.id=id
    def getdetails(self):
        super().getdetails() #call super class method explictly
        print("Company of the employee is",self.cname,"and","id is",self.id)

e=Employee()
e.setdetails("Scott",25)
e.setinfo("Precursor",101)
e.getdetails()


