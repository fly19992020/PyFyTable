from core import core

print("Welcome to PyFyTable")


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
        p = input(">>")
        try:
            command = core.Command(p)
        except:
            print('Error:File"' + p + '"is not found.Code 10')
    elif n == "WRITE":
        i = input(">>").split(",")
        if ln(i):
            command.write(i[0], i[1])
        else:
            print(
                "Error:The coordinates you enter do not look like a correct coordinate. Code 31"
            )
    elif n == "READ":
        i = input(">>")
        while not (ln(i)):
            i = input("Please re-enter it>>").split(",")
        r = command.read(i)
        print(r)
    elif n == "EXIT":
        try:
            command.close()
        except AttributeError:
            pass
        finally:
            exit()
    elif n == "SAVE":
        command.save()
    elif n == "":
        pass
    else:
        print('Error:"' + n + '" is not found.Code 30')
        continue
