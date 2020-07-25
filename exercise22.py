print("Enter 5 numbers:")
numbers = []
for i in range(5):
    n = int(input())
    numbers.append(n)
for i in range(5):
    if numbers[i] > 0:
        print("POSITIVE")
    else:
        print("NEGATIVE")
