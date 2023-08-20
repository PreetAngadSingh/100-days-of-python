# emulating do-while in python
while True:
    number = int(input("Enter the number here : "))
    if not number < 30:
        break
    print("You entered the right number")

print("Exited the while loop")