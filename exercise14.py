product = int(input("The cost of the product: "))
print("---LOCATION---")
print("1. US")
print("2. EUROPE")
print("3. CANADA")
print("4. OTHER")
print("--------------")
region = int(input("Select the number of your region: "))

if region == 1:
    tax = 5
elif region == 2:
    tax = 7
elif region == 3:
    tax = 3
else:
    tax = 9
print("--------------")
print("You have to pay", product+tax, "$.", product, "$ for the product and", tax, "$ for shipping cost.")

