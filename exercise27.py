print("***Sign up***")
username = input("Username: ")
password = input("Password: ")
i = 0
while i < 3:
    print("***Log in***")
    u = input("Username: ")
    p = input("Password: ")
    if username == u and password == p:
        print("Welcome!")
        break
    else:
        print("Wrong username or password.")
        i = i + 1

print("Try again later.")
