course="Python"
print(len(course))

x=len(course)
print(x)

userid="    scott@gmail.com   "
print(userid.strip())

print(course.upper())

frequency=course.count("t",0,len(course))
print(frequency)

name=input("Enter your name")
character=input("Enter the character")
frequency=name.count(character,0,len(name))
print(frequency)

info="python is easy, python is simple learn"
frcount=info.count("python",0,len(info))
print(frcount)

#check email
email=input("Enter your email ID")
pos=email.find("@")
pos1=email.find(".")
if pos==-1 or pos1==-1:
    print("Invalid email")
else:
    print("You can do login")

studentnames="scott,smith,jhon"
for name in studentnames.split(","):
    print(name.title())