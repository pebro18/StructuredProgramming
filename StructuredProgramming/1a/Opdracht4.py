def CheckPalindroom(word):

    if word[0] == word[-1]:
        CheckPalindroom(word[1:-2])
    else:
        return False   
    return True

inputString = input("geef een palindroom: ")

print(CheckPalindroom(inputString))