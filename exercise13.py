import math

hrs = int(input("How many hours has user spent using the charger? "))

member = input("Is this user a member? (yes/no) ")
if member == "yes":
    total = 2*hrs + (10*2*hrs)/100
    print("The user is a member. The user stayed for", hrs, "hours and the total amount is", total, "$.")
else:
    total = 5*hrs + (20*5*hrs)/100
    print("The user is not a member. The user stayed for", hrs, "hours and the total amount is", total, "$.")