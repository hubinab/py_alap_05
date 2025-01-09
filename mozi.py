szotarlista = []
with open("mozi_stat.txt","r",encoding="utf-8") as filebe:
    sorok = filebe.read().splitlines()
    for i in range(1,len(sorok)):
        sor = sorok[i].strip().split(";")
        szotarlista.append({"ev":sor[0],"mozi":sor[1],"befogado":sor[2],"eloadas":sor[3],"latogatas":sor[4],"jegyar":sor[5],"film":sor[6],"mfilm":sor[7]})

latogatottsag = 0

for i in range(len(szotarlista)):
    latogatottsag += int(szotarlista[i]["latogatas"])

print(f"1.feladat: A magyar mozik átlagos látogatottsága: {round(latogatottsag/1000,2)} millió néző")

kettootven = 0

for i in range(len(szotarlista)):
    if int(szotarlista[i]["eloadas"]) >= 250:
        kettootven += 1

print(f"2.feladat: Legalább 250 filmet {kettootven} évben mutattak be.")

volte = False

for i in range(len(szotarlista)):
    if int(szotarlista[i]["jegyar"]) * int(szotarlista[i]["latogatas"]) * 1000 <= 10000000000:
        volte = True
        break

if volte:
    print("3.feladat: Volt 10 milliárd forintnál kisebb árbevételű év.")

legtobbmagyarindex = 0
maxarany = 0
for i in range(len(szotarlista)):
    film = int(szotarlista[i]["film"]) - int(szotarlista[i]["mfilm"])
    mfilm = int(szotarlista[i]["mfilm"])
    arany =  mfilm/film
    if arany > maxarany:
        maxarany = arany
        legtobbmagyarindex = i

print(f"4.feladat: Legtöbb magyar film {round(maxarany*100,2)} % - {szotarlista[legtobbmagyarindex]["ev"]}")

