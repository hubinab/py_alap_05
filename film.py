def leggyakoribb (lista, betu):
    legtobb = 0
    elem = ""
    for i in range(len(lista)):
        if lista[i].count(betu) > legtobb:
            legtobb = lista[i].count(betu)
            elem = lista[i]
    return elem


print("Adjon meg filmcímeket!")
filmlista = []
i = 0
film = "#"
while film != "":
    i += 1
    film = input(f"{i}: ")
    filmlista.append(film)

betu = input("Adja meg a kedvenc betűjét! ")

print(f"Az ajánlott film: {leggyakoribb(filmlista, betu)}")
