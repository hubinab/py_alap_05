penz = int(input("Adja meg a megtakarított pénzét (Ft)! "))
jegy = int(input("Mennyibe kerül egy mozijegy (Ft)? "))

if penz < 0 or jegy < 0:
    print("Hibás a bemenő adat.")
else:
    print(f"A megtakarított pénzből {penz//jegy} mozijegyet lehet vásárolni.")
