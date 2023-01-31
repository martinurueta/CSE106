val = input("Enter a 2 or more number seperated by space: ")
val = val.split()
sum = 0
for i in val:
    sum += int(i)
print("Sum of the numbers is: ", sum)