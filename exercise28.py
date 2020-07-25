import time
seconds = int(input("Enter the number of seconds: "))
countdown = []
for k in range(seconds):
    countdown.append(k+1)
if seconds > 0:
    for i in range(seconds):
        print(seconds)
        time.sleep(1)
        seconds = seconds - 1
        if seconds == 0:
            print("GO!")
else:
    print("Quit.")