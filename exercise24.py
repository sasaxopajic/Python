print("Enter numbers:")
numbers = []
sum = 0
for i in range(10):
    n = int(input())
    if n <= 0:
        break
    sum = sum + n

print("Sum =", sum)