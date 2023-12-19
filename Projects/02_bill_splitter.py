print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip woulf you like to give? 10,12,or 15? "))
people = int(input("How many people to split the bill? "))

total_tip = bill*tip_percentage/100
splitted_bill = round((bill+total_tip)/people,2)

print("Each person should pay: ", splitted_bill)