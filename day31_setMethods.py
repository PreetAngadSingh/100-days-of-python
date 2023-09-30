s1={1,2,5,6}
s2={3,6,7}
#the below line will not update s1 and s2
print(s1.union(s2))
# if you want to update s1
s1.update(s2)
print("s1 after update ",s1)

s1={1,2,5,6}
print(s1.intersection(s2))
print("s1 before update ",s1)
s1.intersection_update(s2)
print("s1 after update ",s1)

s1={1,2,5,6}
# to check if two sets are disjoint
s1.isdisjoint(s2)
# to add an element to the set 
s1.add(7)
print(s1)

# remove throws error if the element is not present in the
# set - this is also important if we intentionally want to raise error
# s1.remove(8)

#  discard doesnt throw error if the element is not present in the set 
s1.discard(8)

if 1 in s1:
    print(1,"is present in s1")
else:
    print(1,"is not present in s1")

item = s1.pop()
print("pop a random element", item, " got pop in ", s1)

#  to clear the set
s1.clear()
print(s1)

# used to delete the set
del s1
# print(s1)

