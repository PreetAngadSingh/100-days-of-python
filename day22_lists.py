marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]

print("This is the list",marks)
print("This is the type of the list",type(marks))
print("Below are the elements of the list")
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

# remember the type of the input/variable
print("Print 'Yes' if '6' is in the list")
if "6" in marks:
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
print("Print 'Yes' if 'Ha' is a part of 'Harry' string")
if "Ha" in "Harry":
  print("Yes")

# print whole list
print("Different ways to output list")
print(marks)
print(marks[:])

# print list but in between index 
print(marks[1:9])
print(marks[:9])
# print list but in between index with jump index as third parameter
print(marks[1:9:3])

# prints square of all numbers less than 10 
print("Playing with lists")
lst = [i*i for i in range(10)]
print(lst)

# prints square of all numbers less than 10 if it is an even number 
lst = [i*i for i in range(10) if i%2==0]
print(lst)