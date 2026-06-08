def iq(x):
    k = 0
    for y in x[0:-1]:
        print(y)
        k +=1
    return k == x[-1]

print(iq(["1", "1", "2", "3", "5"]))
s = iq(["a", "b", "c"])

if s:
    print("sejer")
else:
    print()