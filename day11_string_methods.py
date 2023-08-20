a = "!!Preet!! !!!!  Preet"
print(len(a))
print(a)
# converts string to upper case 
print(a.upper())
# converts string to lower case 
print(a.lower())
# string ! from the end of the string - only trailing ! are stripped
print(a.rstrip("!"))
# replace all occurances of the substring inside the variable
print(a.replace("Preet", "John"))
# split the string with some character 
print(a.split(" "))

blogHeading = "introductiOn to jS"
# turn the first character to upper case and rest as lower case
print(blogHeading.capitalize())
# aligns the string to the center as per the parameters given by the user
print(blogHeading.center(50))
print(a.count("Preet"))
# this returns true/false and checks if the string ends with the given string
print(a.endswith("et"))

# this means that the substring from index 4 to 9 ends with to and returns boolean
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

# finds the substring and returns the index
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("ishh"))
# if the substring is not found, index throws error
# print(str1.index("ishh"))

# returns true if all the elements in the string are alpha numeric A-Z a-z 0-9
# returns true if all the elements in the string are alphabets A-Z a-z
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

# returns true if all characters of the string are lowercase
str1 = "hello world"
print(str1.islower())


# returns true if all characters of the string are printable - note \n is not printable so it returns false
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())

# returns true if all characters are whitespace
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

# returns true only if first character of each word is capitalize
str1 = "World Health Organization" 
print(str1.istitle())

# returns false because first character of each word is not capitalize
str2 = "To kill a Mocking bird"
print(str2.istitle())

# this means that the substring from index 4 to 9 starts with to and returns boolean
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

# makes lower case upper and vice versa
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

# convers the string into title case(capitalize each word)
str1 = "His name is Dan. Dan is an honest man."
print(str1.title())