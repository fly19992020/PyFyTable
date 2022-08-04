print("Welcome to help.py")
while True:
    n = input("HELP? ")
    if n == "ABOUT":
        print("version:v1.1.0")
        print("GPT license")
    elif n == "ALL_COMMAND":
        print("OPEN")
        print("WRITE")
        print("READ")
        print("SAVE")
        print("EXIT")
    elif n == "":
        pass
    else:
        print("Please re-enter it")
