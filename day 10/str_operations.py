# example
fruit = "Mango"
# get length of the string 
fruitLength = len(fruit)
print(fruit,"is a", fruitLength, "letter word")
# get first 4 characters of the string - means including 0 but not 4
print(fruit[0:4])
# this is same as fruit[0:4]
print(fruit[:4])
# this is same as fruit[0:fruitLength]
print(fruit[:])
# this slices from length 0 to len-3
print(fruit[0:len(fruit)-3])
# this is similar to above program
print(fruit[0:-3])
# this will print nothing as this means [4:2]
print(fruit[-1:-3])
# this is same as [2:4]
print(fruit[-3:-1])

# Quick quiz 
nm = "Preet"
print(nm[-4:-2])