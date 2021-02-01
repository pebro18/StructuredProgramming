
def insertionsort(lijst):
    for x in range(len(lijst)):
        for y in range(x,-1,-1):
            if lijst[y] < lijst[x]:
                tempX = lijst[x]
                lijst[x] = lijst[y]
                lijst[x+1] = tempX
    pass

print()