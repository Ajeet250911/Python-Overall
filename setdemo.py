numberset={1,89,24,78}
for num in numberset:
    print(num)

colorset={"cyan","white","red"}
for c in colorset:
    print(c)

colorset.add("green") #add in set
print(colorset)

#colorset.discard("yellow") #remove with error
#print(colorset)

#colorset.remove("yellow") #remove with error
#print(colorset)

colorset1={"white","blue","pink"}
# colorset.update(colorset1)
# print(colorset)

inter_set=colorset1.intersection(colorset)
print(inter_set)

union_set=colorset1.union(colorset)
print(union_set)