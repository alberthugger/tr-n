import random
import math

D_Liv = 100
M1_Liv=100
M2_Liv=100
M3_Liv=100
Våben = 10

while D_Liv >=0:

    m = math.floor(random.random() * 20)
    print()
    print("Vil du?")
    print("Angribe, svar 1")
    print("Forsvare, svar 2")
    print("Løbe, sver 3")
    print("Monsteret giver " + str(m))
    c = input()
    if c == "1":
        D_Liv-=m
        M1_Liv-=Våben
    elif c == "2":
        D_Liv-=m/2
    
    if M1_Liv <= 0:
        print("You win!")
        break
    elif D_Liv <= 0:
        print("You die!")
        break

    print()
    print("Dit livs total " + str(D_Liv))
    print("Monsters livs total " + str(M1_Liv))