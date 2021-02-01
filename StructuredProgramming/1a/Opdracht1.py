# Opdracht 1
InputRange = int(input("Hoe groot de lengte: "))

for x in range(0,InputRange + 1):

    OutputString = '*' * x
    print(OutputString)
    pass

for x in range(InputRange - 1,0,-1):
    OutputString = '*' * x
    print(OutputString)
    pass

i = 0
while (i <= InputRange):
    
    OutputString = '*' * i
    print(OutputString)
    i+= 1
    pass

while (i >=0):
    OutputString = '*' * i
    print(OutputString)
    i += -1
    pass
