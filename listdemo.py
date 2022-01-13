course_list=["python","java","android","reactjs"]
#print(course_list[0]) #list items can be fetched using index position

# for course_name in course_list:
#     print(course_name)


# numberlist=[10,20,30,40]
# for num in numberlist:
#     print(num)

print(len(course_list))
course_list.append("django")
print(course_list)

new_course_list=["angular","flask"]
course_list.extend(new_course_list)
print(course_list)

course_list.sort()
print(course_list)

course_list.reverse()
print(course_list)

print(max(course_list))

# course_list.pop()
# print(course_list)

course_list.pop(2)
print(course_list)

