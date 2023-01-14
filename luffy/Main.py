###############################
#          PyTyTable          #
#           v2.0.0            #
#     Another:Fly19992020     #
#     GNU GPL License v3.0    #
###############################


import load

print("Welcome to PyFyTable")
ho = False

mainDir = load.mainDir

while True:
    n = input("PFT[ ")
    if n in mainDir:
        mainDir[n]()
    elif n == "":
        pass
    else:
        print("Error:\"{input}\" is not found.Code 30".format(input=n))
