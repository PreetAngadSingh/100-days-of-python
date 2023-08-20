l = [11,45,1,2,3,4,6]
print(l)

# append()
l.append(7)
print(l)

# sort()
l.sort()
print(l)

# reverse()
l.reverse()
print(l)

# index() - returns the index of the first occurance of the parameter
print(l.index(1))

#count() - returns the count of the parameter inside the list
print(l.count(1))

#copy() - creates a copy of the list
# m = l.copy()

#insert() - at a particular index
l.insert(1, 899)

# extend()
m = [900,1000,1100]

# if you dont want to change l list
k=l+m
print(k)

#this will change the l list
l.extend(m)
print(l)
