###############################
#          PyTyTable          #
#           v2.0.0            #
#     Another:Fly19992020     #
#     GNU GPL License v3.0    #
###############################

if __name__ == "__main__":
    import load

def set_command(c):
    global command
    command = c

if __name__ == "__main__":
    # used to load the libs
    mainDir = {}
    import importlib
    f = open("libs.txt", mode="r", encoding="utf-8")
    libs = f.read().split("\n")
    for i in libs:
        try:
            lib = importlib.import_module("libs." + i)
        except ModuleNotFoundError:
            print("Error: The module \"{module}\" is not found.".format(module=i))
            exit(1)
        print (lib.dire)
        try:
            funcs = lib.dire
            mainDir.update(funcs)
        except AttributeError:
            print("Error: The module \"{module}\" does not have a dire attribute.".format(module=i))
            exit(1)


    print("Welcome to PyFyTable")
    ho = False

    mainDir.update(load.mainDir)
    command = None # create the command object.
    while True:
        n = input("PFT[ ")
        if n in mainDir:
            mainDir[n](command)
        elif n == "":
            pass
        else:
            print("Error:\"{input}\" is not found.Code 30".format(input=n))
