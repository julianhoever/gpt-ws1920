def summe():
    zahl = int(input("Zahl: "))
    if zahl == 0:
        return 0
    return zahl + summe()
