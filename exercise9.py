import math

print("Tip: Grades range from 0 - 10!")

a = int(input("Algebra: "))
g = int(input("Geometry: "))
p = int(input("Physics: "))

avg = a + g + p
avg = round(avg, 2)

if avg >= 7:
    print("Your average score is", avg, ". Good job!")
elif 4 <= avg <= 6:
    print("Your average score is", avg, ". You need to work harder!")
else:
    print("Your average score is", avg, ". Failed!")