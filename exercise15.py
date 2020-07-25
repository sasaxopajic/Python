call = int(input("How many seconds was the call's duration? "))

if call <= 500:
    price = call*0.01
elif 501 <= call <=800:
    price = 500*0.01 + (call-500)*0.008
else:
    price = 500*0.01 + 300*0.008 + (call-800)*0.005

print("Total amount: ", price, "$.")