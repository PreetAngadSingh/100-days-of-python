# the break statement exits the for loop as soon as it is executed
for i in range(12):
    if(i==10):
        break
    print("5 X", i+1, "=", 5*(i+1))

print("the loop has been broken")

# the continue statement skips that iteration within the for loop
for j in range(12):
    if(j==10):
        print("the iteration is skipped")
        continue
    print("5 X", j+1, "=", 5*(i+1))
