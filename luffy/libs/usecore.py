import importlib
import luffy.Main as Main
core = importlib.import_module("luffy.core")
ho = False # has open a file.


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


def pft_open(command):
    global ho
    p = input(">> ")
    he = False  # has error
    try:
        Main.set_command(core.Command(p))
        command = core.Command(p) # create the command object.
    except FileNotFoundError:
        print("Error:File\'{path}\"is not found.Code 10".format(path=p))
        he = True
    if not he:
        ho = True  # has open
    if ho:
        for i in range(len(command.pftcl)):
            sp = command.pftcl[i].split(":")
            if len(sp) != 2 and len(sp) != 1:
                print("Warning: There is an unrecognized item.")
                command.pftcl.pop(i)
    else:
        print("Warning:This file failed to open. Code 12.")


def write(command):
    if ho:
        i = input(">> ").split(",")
        sn = ln(i[0])  # user's input is true
        if sn:
            command.write(i[0], i[1])
        else:
            print(
                "Error:The coordinates you enter do not look"
                "like a correct coordinate. Code 31"
            )
    else:
        print("Error:You have not opened a file. Code 20.")


def read(command):
    if ho:
        i = input(">> ")
        sn = ln(i)  # user's input is true
        if sn:
            print(command.read(i))
        else:
            print(
                "Error:The coordinates you enter do not look"
                "like a correct coordinate. Code 31"
            )
    else:
        print("Error:You have not opened a file. Code 20.")


def pft_exit(command):
    if ho:
        command.close()
    exit()


def save(command):
    if ho:
        command.save()
    else:
        print("Error:You have not opened a file. Code 20.")


dire = {"OPEN": pft_open, "WRITE": write, "READ": read, "EXIT": pft_exit, "SAVE": save}
