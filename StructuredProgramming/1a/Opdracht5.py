
def insert(lst, grens, waarde):
    for x in range(grens,-1,-1):
        if waarde < lst[x]:
            tempX = lst[x]
            lst[x] = waarde
            lst[x+1] = tempX
            pass
        pass

def insertionsort(lijst):
    lst = lijst.copy()
    for x in range(0,len(lst)):
        insert(lst,x,lst[x])
    return lst


lst = [1,6,14,7,21,7]
lst = insertionsort(lst)
print(lst)