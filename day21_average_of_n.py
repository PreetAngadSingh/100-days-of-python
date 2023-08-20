# find average of n numbers
def nAverage(*numbers):
    sum=0
    for number in numbers:
        sum = sum + number
    print('Average is : ', sum/len(numbers))

nAverage(5, 6, 7)   