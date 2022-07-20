from core import core
print("Welcome to PyFyTable")
command = core.Command()


def ln(c):
    c = list(c)
    while True:
        if c[-1].isdigit():
            c.pop(-1)
        else:
            break
    r = False
    c = "".join(c)
    r = c.isalpha()
    return r


while True:
    n = input("PFT[")
    if n == "OPEN":
        l = input(">>")
        while not(ln(l)):
            l = input("Please re-enter it>>").split(",")
        command.open(l)
    elif n == "WRITE":
        l = input(">>").split(",")
        while not(ln(l[0])):
            l = input("Please re-enter it>>").split(",")
        command.write(l[0], l[1])
    elif n == "READ":
        l = input(">>")
        r = command.read(l)
        print(r)
    elif n == "EXIT":
        command.close()
        exit()
    elif n == "SAVE":
        command.save()
    else:
        print("Please re-enter it.")
        continue
