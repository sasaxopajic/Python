x = int(input("Enter a number: "))

while x > 10:
    y = x % 10
    if y <= 10:
        break
else:
    y = x % 10

print("The last digit of the number is", y, ".")
