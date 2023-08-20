# this code will help understand how functions work
def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

# this function is defined but will not execute without errors
def isLesser(a, b):
    pass

a = 9
b = 8
calculateGmean(a,b)

c = 5
d = 4
calculateGmean(c,d)
