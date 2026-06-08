import random
import math
import collections

while True:
    Spiller_1s_kort = 0
    Spiller_2s_kort = 0

    kort = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    M = kort.count(0) + kort.count(1)-1
    x = 0
    while x < M/2:
        a = random.randint(0, M)
        if 0 == kort[a]:
            kort[a] = 1
            x +=1

    while True:
        Spiller_1s_kortbunge = (kort.count(0))
        Spiller_2s_kortbunge = (kort.count(1))

        print()

        if Spiller_1s_kortbunge == 0:
            print()
            print()
            print()
            print("Du tabte spillet!")
            print("___________________________________________")
            break
        elif Spiller_2s_kortbunge == 0:
            print()
            print()
            print()
            print("Du vandt spillet!")
            print("___________________________________________")
            print()
            break

        print("Antal kort du har tilbage: " + str(Spiller_1s_kortbunge))

        while True:
            Spiller_1s_kort = random.randint(0, M)
            if 0 == kort[Spiller_1s_kort]:
                Spiller_1s_kort = Spiller_1s_kort
                Spiller_1s_kort = math.ceil(Spiller_1s_kort)
                print("Dit kort er: " + str(Spiller_1s_kort))
                break
        while True:
            Spiller_2s_kort = random.randint(0, M)
            if 1 == kort[Spiller_2s_kort]:
                Spiller_2s_kort = Spiller_2s_kort
                Spiller_2s_kort = math.ceil(Spiller_2s_kort)
                print("Modstanderens kort er: " + str(Spiller_2s_kort))
                break

        if Spiller_1s_kort < Spiller_2s_kort:
            int(Spiller_1s_kort)
            kort[Spiller_1s_kort] = 1
            print("Du tabte denne runde.")
        elif Spiller_2s_kort < Spiller_1s_kort:
            int(Spiller_2s_kort)
            kort[Spiller_2s_kort] = 0
            print("Du vandt denne runde.")
        else:
            print("Uafgjort")
        
        print()
        print("___________________________________________")
        control = input("Klar igen? ") 
        if control == "Dæk":
            print(kort)
        elif control == "Genstart":
            break
        
