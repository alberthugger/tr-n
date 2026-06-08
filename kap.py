Liv = 10
Porsens = 3
def kamp(x):
    c = []
    for y in x:
        c.append(input(y))
    return c

int(input())

print(kamp)
print("Liv: " + str(Liv))
print("Porsens: " + str(Porsens))

if k[0] == "y":
    Liv-=1
if k[1] == "y":
    Porsens-=1
    Liv+=3

print("Liv: " + str(Liv))
print("Porsens: " + str(Porsens))

k = dig(["Slå: ","Porsen: ","Låp: "])

if k[0] == "y":
    Liv-=1
if k[1] == "y":
    Porsens-=1
    Liv+=3

print("Liv: " + str(Liv))
print("Porsens: " + str(Porsens))

