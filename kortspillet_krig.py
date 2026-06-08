import random
import math
spiller_1s_kortbunke = 0
spiller_2s_kortbunke = 0
spiller_1s_kort = 0
spiller_2s_kort = 0

x = math.floor(random.random() * 10)
if x <= 6:
    kort_1 = [1,True]
    spiller_1s_kortbunke +=1
else:
    kort_1 = [1,False]
    spiller_2s_kortbunke +=1

x = math.floor(random.random() * 10)
if x <= 6:
    kort_2 = [2,True]
    spiller_1s_kortbunke +=1
else:
    kort_2 = [2,False]
    spiller_2s_kortbunke +=1

x = math.floor(random.random() * 10)
if x <= 6:
    kort_3 = [3,True]
    spiller_1s_kortbunke +=1
else:
    kort_3 = [3,False]
    spiller_2s_kortbunke +=1

x = math.floor(random.random() * 10)
if x <= 6:
    kort_4 = [4,True]
    spiller_1s_kortbunke +=1
else:
    kort_4 = [4,False]
    spiller_2s_kortbunke +=1

x = math.floor(random.random() * 10)
if x <= 6:
    kort_5 = [5,True]
    spiller_1s_kortbunke +=1
else:
    kort_5 = [5,False]
    spiller_2s_kortbunke +=1

x = math.floor(random.random() * 10)
if x <= 6:
    kort_6 = [6,True]
    spiller_1s_kortbunke +=1
else:
    kort_6 = [6,False]
    spiller_2s_kortbunke +=1

def spiller_1s_runde():
    while True:
        x = random.randint(1, 6)
        if x == 1:
            if kort_1[1] == True:
                print("Du trækker: " +  str(kort_1[0]))
                return(1)
        elif x == 2:
            if kort_2[1] == True:
                print("Du trækker: " +  str(kort_2[0]))
                return(2)
        elif x == 3:
            if kort_3[1] == True:
                print("Du trækker: " +  str(kort_3[0]))
                return(3)
        elif x == 4:
            if kort_4[1] == True:
                print("Du trækker: " +  str(kort_4[0]))
                return(4)
        elif x == 5:
            if kort_5[1] == True:
                print("Du trækker: " +  str(kort_5[0]))
                return(5)
        elif x == 6:
            if kort_6[1] == True:
                print("Du trækker: " +  str(kort_6[0]))
                return(6)

def spiller_2s_runde():
    while True:
        x = random.randint(1, 6)
        if x == 1:
            if kort_1[1] == False:
                print("Modstanderen trækker: " +  str(kort_1[0]))
                return(1)
        elif x == 2:
            if kort_2[1] == False:
                print("Modstanderen trækker: " +  str(kort_2[0]))
                return(2)
        elif x == 3:
            if kort_3[1] == False:
                print("Modstanderen trækker: " +  str(kort_3[0]))
                return(3)
        elif x == 4:
            if kort_4[1] == False:
                print("Modstanderen trækker: " +  str(kort_4[0]))
                return(4)
        elif x == 5:
            if kort_5[1] == False:
                print("Modstanderen trækker: " +  str(kort_5[0]))
                return(5)
        elif x == 6:
            if kort_6[1] == False:
                print("Modstanderen trækker: " +  str(kort_6[0]))
                return(6)

while True:          
    if spiller_1s_kortbunke == 0:
        print("Du tabte spillet")
        break
    elif spiller_2s_kortbunke == 0:
        print("du vandt spillet!")
        break

    print()
    print()
    print("Antallet af kort i din kortbunke er " + str(spiller_1s_kortbunke))

    print()
    spiller_1s_kort = spiller_1s_runde()
    spiller_2s_kort = spiller_2s_runde()

    if spiller_1s_kort >= spiller_2s_kort:
        print("Du vandt runden")
        spiller_1s_kortbunke +=1
        spiller_2s_kortbunke -=1
        if spiller_2s_kort == 1:
            kort_1[1] = True
        elif spiller_2s_kort == 2:
            kort_2[1] = True
        elif spiller_2s_kort == 3:
            kort_3[1] = True
        elif spiller_2s_kort == 4:
            kort_4[1] = True
        elif spiller_2s_kort == 5:
            kort_5[1] = True
        elif spiller_2s_kort == 6:
            kort_6[1] = True
    elif spiller_2s_kort >= spiller_1s_kort:
     print("Du tabte runden")
     spiller_1s_kortbunke -=1
     spiller_2s_kortbunke +=1
     if spiller_1s_kort == 1:
         kort_1[1] = False
     elif spiller_1s_kort == 2:
         kort_2[1] = False
     elif spiller_1s_kort == 3:
         kort_3[1] = False
     elif spiller_1s_kort == 4:
        kort_4[1] = False
     elif spiller_1s_kort == 5:
         kort_5[1] = False
     elif spiller_1s_kort == 6:
         kort_6[1] = False
    input()
