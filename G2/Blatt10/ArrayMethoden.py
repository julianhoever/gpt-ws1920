import sys

def summe(arr):
    s = 0
    for zahl in arr:
        s += zahl
    return s

def multi(arr):
    p = 1
    for zahl in arr:
        p *= zahl
    return p

def doppel(arr):
    d = []
    for zahl in arr:
        d += [zahl, -zahl]
    return d

if len(sys.argv) <= 2:
    print("Nicht genug Parameter angegeben!")
else:
    zahlen = []
    try:
        for i in range(1, len(sys.argv)-1):
            zahlen += [float(sys.argv[i])]
    except:
        print("Ungültige Zahl übergeben!")
    else:
        if sys.argv[-1] == "s":
            print(summe(zahlen))
        elif sys.argv[-1] == "m":
            print(multi(zahlen))
        elif sys.argv[-1] == "d":
            print(doppel(zahlen))
        else:
            print("Ungültige Methode übergeben!")
