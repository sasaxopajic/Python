print("Which meal do you want to buy?")
print("1. Burger")
print("2. Pizza")
print("3. Hot Dog")
print("----------")
m = input("Choose your meal: ")
print("----------")
if m == "Burger":
    print(m, "5$.")
elif m == "Pizza":
    print(m, "3$.")
elif m == "Hot Dog":
    print(m, "1.5$.")