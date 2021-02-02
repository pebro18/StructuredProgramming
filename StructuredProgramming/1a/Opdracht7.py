import random

randomnumber = random.randint(0,10)

while True:
    Guess = int(input("Raad het nummer 1 tot 10: "))
    if Guess == randomnumber:
        print('Je hebt het nummer geraden')
        break
        pass
    pass
