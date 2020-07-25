print("Wage: 400$")
x = int(input("The number of years employed: "))
y = int(input("The number of children the employee has: "))
z = int(input("The number of missed days: "))

if z == 0:
    total = int(400 + 20*x + 30*y + 100)
    print("The total amount is", total, "$. 400$ minimum wage +", 20*x, "$ for", x, "years experience +", 30*y, "$ for", y, "kids + 100 $ for not missing a day at work.")
else:
    total = int(400 + 20*x + 30*y)
    print("The total amount is", total, "$. 400$ minimum wage +", 20*x, "$ for", x, "years experience +", 30*y, "$ for", y, "kids.")