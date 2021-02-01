# Opdracht 10
inputlimit = int(input("Voer in limiet voor Fibonaci nummer: "))


def Fibonaci(looplst = [0,1]):
    
    lst = looplst

    #base line
    if len(lst) == inputlimit + 1:
        return lst
    # recursief
    nextnumber = lst[-2] + lst[-1]
    lst.append(nextnumber)
    Fibonaci(lst)

    return lst[-1]

print(Fibonaci())