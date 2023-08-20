import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

# getting hours of the current time
hours = int(time.strftime('%H'))

# writing the if else statements
if(hours>=5 and hours<12):
    print("Good Morning")
elif(hours>=12 and hours<17):
    print("Good Afternoon")
elif(hours>=17 and hours<22):
    print("Good Evening")
else:
    print("Good Night")
