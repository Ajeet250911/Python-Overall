marks_dict={101:[45,57,50],
            102:[36,46,45],
            103:[45,47,40]
            }
#print(marks_dict)

for marks in marks_dict.items():
    #print(marks)
    print("Rollnumber ",marks[0])
    #print("Marks ",marks[1])
    print("Marks is as follows")
    for mk in marks[1]:
        print(mk,end="")
        print("")

for mk in marks_dict.values():
    # print(mk)
    for m in mk:
        print(m,end=" ")
    print("")



