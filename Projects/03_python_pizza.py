print("Thank you for choosing python pizza")
size = input("What size of pizza do you want?\nS : Small\nM : Medium\nL : Large\n")
amount=0
if(size == "S"):
    amount=15
elif(size == "M"):
    amount=20
else:
    amount=25

add_pepperoni = input("Do you want to add pepperoni? (Y or N)\n")
if(add_pepperoni == "Y" and size == "S"):
    amount+=2
elif(add_pepperoni == "Y"):
    amount+=3

add_cheese = input("Do you want to add cheese? (Y or N)\n")
if(add_cheese == "Y"):
    amount+=1

print("Your final bill is: $",amount)