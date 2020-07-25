import math
print("Enter 5 numbers:")
sum = 0
for i in range(5):
    n = int(input())
    sum = sum + n
avg = sum/5
avg = round(avg, 2)
print("Average number:", avg)
