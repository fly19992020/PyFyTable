from core import core

print("Welcome to PyFyTable")
ho = False


def ln(c):
    c = list(c)
    hd = False  # has digit
    while True:
        try:
            thd = c[-1].isdigit()  # this is digit
        except IndexError:
            thd = False
        if thd:
            hd = True
            c.pop(-1)
        else:
            break
    if hd:
        c = "".join(c)
        r = c.isalpha()
    else:
        r = False
    return r


while True:
    n = input("PFT[")
    if n == "OPEN":  # open
        p = input(">>")
        he = False  # has error
        try:
            command = core.Command(p)
        except FileNotFoundError:
            print("Error:File\'{path}\"is not found.Code 10".format(path=p))
            he = True
        if not he:
            ho = True  # has open
        if ho:
            for i in range(len(command.pftcl)):
                sp = command.pftcl[i].split(":")
                if len(sp) != 2 and len(sp) != 0:
                    print("Warning: There is an unrecognized item.Code 11")
                    command.pftcl.pop(i)
                elif len(sp) == 0:
                    command.pftcl.pop(i)

    elif n == "WRITE":  # write
        if ho:
            i = input(">>").split(",")
            sn = ln(i[0])  # user's input is true
            if sn:
                command.write(i[0], i[1])
            else:
                print(
                    "Error:The coordinates you enter do not look"
                    "like a correct coordinate. Code 31"
                )
        else:
            print("Error: You have not opened a file. Code 20.")

    elif n == "READ":  # read
        if ho:
            i = input(">>")
            sn = ln(i)  # user's input is true
            if sn:
                print(command.read(i))
            else:
                print(
                    "Error:The coordinates you enter do not look"
                    "like a correct coordinate. Code 31"
                )
        else:
            print("Error: You have not opened a file. Code 20.")

    elif n == "EXIT":  # exit
        if ho:
            command.close()
        exit()

    elif n == "SAVE":  # save
        if ho:
            command.save()
        else:
            print("Error: You have not opened a file. Code 20.")

    elif n == "":
        continue

    else:
        print('Error:\"{input}\" is not found.Code 30'.format(input=n))
        continue
