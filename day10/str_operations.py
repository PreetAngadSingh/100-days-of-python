# example
fruit = "Mango"
# get length of the string 
fruitLength = len(fruit)
print(fruit,"is a", fruitLength, "letter word")
# get first 4 characters of the string 
print(fruit[0:4])
# this is same as fruit[0:4]
print(fruit[:4])
# this is same as fruit[0:fruitLength]
print(fruit[:])
# this slices from length 0 to len-3
print(fruit[0:len(fruit)-3])
print(fruit[0:-3])