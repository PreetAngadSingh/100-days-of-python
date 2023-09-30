#below is a docstring, this will effect the output of the program
# docstring will always be above the defination of the program
#right below the function name, or right above the function body
def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)