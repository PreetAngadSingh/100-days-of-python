# passing an argument inside a function
def average(a,b):
    print((a+b)/2)

average(1,9)

# if parameter is passed, then the argument picks it otherwise the default selection is considered

def name(fname, mname="John", lname="Whatson"):
    print('Hello', fname, mname, lname)

name("Amy")
name("Amy","Agarwal")
name("Amy","Agarwal", "Jain")