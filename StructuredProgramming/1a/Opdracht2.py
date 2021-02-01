# Opdracht 2

InputString1 = input("Geef een String: ")
InputString2 = input("Geef een String: ")

def Give_Index_Of_Diffrence_Of_Two_Strings(String1,String2):
    Index = 0
    lenString1 = len(String1)
    lenString2 = len(String2)
    Shortestlen = min([lenString1,lenString2])

    for x in range(Shortestlen):
        if String1[x] != String2[x]:
            Index = x
            break
            pass
        if x == Shortestlen - 1:
            Index = None
            pass
        pass
    return Index

print("Het eerste verschil zit op index: {}".format(Give_Index_Of_Diffrence_Of_Two_Strings(InputString1,InputString2)))
