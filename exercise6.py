price = int(input("Laptop price: "))
tax = int(input("Tax percentage: "))

total = int(price + (tax*price)/100)

print("The total price of the laptop is", total, "$.")
