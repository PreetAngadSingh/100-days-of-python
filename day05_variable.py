# variable a of data type integer
a = 9
print(a)
b = 5
name = "Preet Angad"
print(name)

# we cannot do the below operation, because the datatypes are different
# sum = a+name
sum = a+b;
print(sum)

# to know the data type of a variable we use type()
print("The type of a is ", type(a))
print("The type of a is ", type(name))

# different types of data type
list1 = [1, 2.3, [4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Preet", "age":22, "canVote":True}
print(dict1)