#tuple is immutable

gender=("Male","Female","Other")
print(gender)
print(len(gender))

dicnumbers=(1,2,3,4,5,6)
print(max(dicnumbers))
print(min(dicnumbers))

print(type(gender)) #type used to find datatype
print(type(dicnumbers)) #type used to find datatype

#covert tuple into list

branchtuple=("CSE","EC","IT")
branchlist=list(branchtuple) #covert tuple into list
print(type(branchlist))
print(branchlist)

#covert list into tuple

courselist=["java","python"]
course_tuple=tuple(courselist)
print(type(course_tuple))
print(course_tuple)

for branch in branchtuple:
    print(branch,end=",")

print(branchtuple[0])

#tuple constructor

languages=tuple(("Python","Java","C","C++")) #tuple constructor is made by using double parathesis ()
print(languages)

#to delete the tuple
del languages
print(languages)

#for slicing
print(languages[-2])

#for slicing range
print(languages[1:3])
print(languages[0:])

