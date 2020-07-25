import math
n = int(input("Enter a number: "))
sum = 0
for i in range(n+1):
    sum = sum + i
avg = sum/n
avg = round(avg, 1)

print("Average number =", avg)
