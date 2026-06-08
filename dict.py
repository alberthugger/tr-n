fjender = [ {
    "name": "alber",
    "liv": 10
}, {
    "name": "bertr",
    "liv": 20
}, {
    "name": "mekel",
    "liv": 30
} ]

dsdsd
def fin_f (name):
    for fjende in fjender:
        if fjende["name"] == name:
             print(fjende["liv"])
def tilføj_fjende(name, liv):
    fjender.append({
        "name": name,
        "liv": liv
    })


name = input("hvem vil du angrive")
fin_f (name)
fjender.append({
    "name": "o",
    "liv": 50
})
print(fjender)
