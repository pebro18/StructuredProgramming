InputString = input("Geef een tekst: ")
InputRotation = int(input("Geef een nummer: "))

Output = ""
for x in InputString:   
    shifted = ord(x) + InputRotation
    if shifted > ord('z'):
        shifted -= 26
        pass
    Output += chr(shifted)
    pass
print(Output)