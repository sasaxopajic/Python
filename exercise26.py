x = 1
apartments = []
sum_ap = 0
while x > 0:
    x = int(input("Apartment price: "))
    if x > 0:
        sum_ap = sum_ap + 1
        apartments.append(x)
        print("Apartment", sum_ap, "price:", x)
    else:
        print("Try again!")
        break

sum_price = 0
k = 0
for k in range(len(apartments)):
    sum_price = sum_price + apartments[k]
avg = sum_price/sum_ap

print(sum_ap, "apartments have been registered. The average price for rent is", avg)

y = 1
while y > 0:
    y = int(input("Rent price: "))
    if y > avg:
        print("Above average price.")
    elif y == avg:
        print("Same as average price.")
    elif 0 < y < avg:
        print("Below average price.")
    else:
        print("Quit!")


