import core
print("Welcome to PyFyTable")
command = core.Command()
while True:
    n = input("PFT[")
    if n == "OPEN":
        l = input(">>")
        command.open(l)
    elif n == "WRITE":
        l = input(">>").split(",")
        command.write(l[0], l[1])
    elif n == "READ":
        l = input(">>")
        r = command.read(l)
        print(r)
    elif n == "EXIT":
        exit()
    elif n == "SAVE":
        command.save()
    else:
        print("Please re-enter it.")
        continue
