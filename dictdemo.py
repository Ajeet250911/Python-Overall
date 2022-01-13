citydict={"LKO":"Lucknow",
          "KNP":"Kanpur",
          "VNS":"Varanasi"
          }
print(citydict)
print(type(citydict))

# print(citydict.popitem())
# print(citydict)

# print(citydict.pop("LKO")) #using Key
# print(citydict)

#print the value of that key
print(citydict.get("KNP")) #with function
print(citydict["LKO"]) #without using function  #we will use both ways in Django

#use of update in dictionary
citydict.update({"AGR":"agra"})
print(citydict)

#dict constructor
course=dict(py="Python",java="Core Java",wt="Web Technology") #dict constructor in Django
course["cloud"]="Amazon Web Services" #another way to add in dictionary other than update #will use in Django
print(course)

#use of value in dict
# for name in course.values():
#     #print("course name is "+name)
#     print(f"Course name is {name}")

# for course_code in course.keys():
#     print(f"Course code name is {course_code}")

for data in course.items(): #returns key value pair in form of tuple
    print(data)
    print(type(data))
    #print(data[0])



