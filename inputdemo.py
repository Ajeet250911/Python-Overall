from unicodedata import name

name=input("Enter your name")
age=int(input("Enter your age"))
salary=float(input("Enter the salary"))

print("Hello "+name,"your age is",age)

#printing statement using format specifier
print("Hello %s ,your age is %d" %(name,age))

#using placeholders and format function of str
print("hello {0} your age is {1} and your salary is {2}".format(name,age,salary))

#FString
print(f"hello {name} your age is {age} ")

#use if else in python
if age>=18:
    print(name+" you can do registration")
else:
    print(f"sorry {name} wait for few more years")


