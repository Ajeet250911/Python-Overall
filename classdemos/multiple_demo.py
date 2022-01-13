class BasicPhone:
    def setPhone(self,keypad):
        self.keypad=keypad
    def getPhone(self):
        print("Keypad type is",self.keypad)

class Computer:
    def setComputer(self,ostype):
        self.ostype=ostype
    def getComputer(self):
        print("OS type is",self.ostype)

class SmartPhone(Computer,BasicPhone):
    def setSmartPhone(self,company):
        self.company=company
    def getdetails(self):
        print("Company name is",self.company)

s=SmartPhone()
s.setPhone("Button Keypad")
s.setComputer("Mac IOS")
s.setSmartPhone("Apple")
s.getPhone()
s.getComputer()
s.getdetails()

c=Computer()

print(issubclass(SmartPhone,Computer)) #showing true if the subclass is inherited with superclass
print(issubclass(SmartPhone,BasicPhone))
print(issubclass(BasicPhone,object)) #Every superclass is inherited with builtin superclass #object

print(isinstance(s,SmartPhone)) #Showing the object is of the particular class
print(isinstance(c,BasicPhone)) #no relation thats why showing false

print(SmartPhone.__bases__) # builtin class variable to print the superclass