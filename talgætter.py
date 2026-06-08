import random
import math

c = 0

x = math.floor(random.random() * 100)


while True:
    y = int(input())
    c+= 1
    print("Forså " + str(c))
    if y == x:
        print("Sajer!")
        break
    elif y == 7:
        print("Sajer!")
        break

    elif y < x:
        print("Over")

    elif y > x:
        print("Unne")
    

