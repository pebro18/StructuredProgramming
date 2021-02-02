
for x in range(100):
    OutputString = ""
    if x % 3 == 0:
        OutputString += "fizz"
        pass
    if x % 5 == 0:
        OutputString += "buzz"
        pass
    print("{} {}".format(x,OutputString))
    pass