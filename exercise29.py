drivers_count = 0
earnings = 0
while drivers_count >= 0:
    member = input("Are you already a member? (yes/no) ")
    if member == "yes":
        charge = 1.5
    else:
        charge = 3

    hrs = int(input("How many hours have you been parked? Enter a valid value! "))
    if 0 < hrs <= 1:
        price = 2
    elif 1 < hrs <= 2:
        price = 3.5
    elif 2 < hrs <= 3:
        price = 4.5
    else:
        price = 4.5 + (hrs - 3)*0.5
    total = charge + price
    print("Total: ", total, "$.")

    drivers_count = drivers_count + 1
    earnings = earnings + total

    m = input("Do you want to continue? (yes/no) ")
    if m == "no":
        print(drivers_count, "drivers payed. The total earnings are", earnings, "$.")
        break