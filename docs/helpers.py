print("Welcome to helper.py")
def command(c:str):
    help = {
        "READ":"] rc",
        "WRITE":"] rc,what you want to write",
        "SAVE":"] SAVE",
        "EXIT":"] EXIT"
    }
    try:
        print(help[c])
    except:
        print("Error.")


while True:
    n = input("HELP? ")
    if n == "ABOUT":
        print("version:v2.0.0")
        print("GPT license")
    elif n == "ALL_COMMAND":
        print("OPEN")
        print("WRITE")
        print("READ")
        print("SAVE")
        print("EXIT")
    elif n == "":
        continue
    elif n == "COMMAND":
        while True:
            n2 = input(">")
            if n2 == "&EXIT":
                break
            else:
                command(n2)
    
    elif n == "EXIT":
        exit()

    else:
        print("Please re-enter it")
        continue
