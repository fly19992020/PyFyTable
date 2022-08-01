from core import core

print("Welcome to PyFyTable")


def ln(c):
    c = list(c)
    f = False
    while True:
        if c[-1].isdigit():
            f = True
            c.pop(-1)
        else:
            break
    r = False
    if f:
        c = "".join(c)
        r = c.isalpha()
    else:
        r = False
    return r


while True:
    n = input("PFT[")
    if n == "OPEN":  #open
        p = input(">>")
        try:
            command = core.Command(p)
        except:
            print("Error:File\'{path}\"is not found.Code 10".format(path=p))

    elif n == "WRITE":  #write
        i = input(">>").split(",")
        f = 1  #flag
        try:
            l = ln(i[0])
        except IndexError:
            f = 0
        if f == 1 and l:
            print(command.write(i[0], i[1]))
        else:
            print(
                "Error:The coordinates you enter do not look"
                "like a correct coordinate. Code 31"
            )

    elif n == "READ":  #read
        i = input(">>")
        f = 1  #flag
        try:
            l = ln(i)
        except IndexError:
            f = 0
        if f == 1 and l:
            print(command.read(i))
        else:
            print(
                "Error:The coordinates you enter do not look"
                "like a correct coordinate. Code 31"
            )

    elif n == "EXIT":  #exit
        try:
            command.close()
        finally:
            exit()

    elif n == "SAVE":  #save
        command.save()

    elif n == "":
        continue

    else:
        print('Error:\"{input}\" is not found.Code 30'.format(input=n))
        continue
