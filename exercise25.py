print("FLIP-A-COIN")
print("-----------")
x = str
sum_head = 0
sum_tail = 0

while x != "stop":
    x = input()
    if x == 'head':
        sum_head = sum_head + 1
    elif x == 'tail':
        sum_tail = sum_tail + 1

print("The end!")
print("Head won", sum_head, "times and tail won", sum_tail, "times.")

hp = 100*(sum_head/(sum_head+sum_tail))
tp = 100 - hp
print("Head", hp,"%, tail", tp, "%.")