val = input("Enter 2 or more numbers separated by space: ")
val = val.split()
sum = 0
for i in val:
    sum += float(i)
print("Sum of the numbers is: ", sum)
