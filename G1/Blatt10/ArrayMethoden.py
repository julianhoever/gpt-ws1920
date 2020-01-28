import sys

def summe(arr):
    s = 0
    for zahl in arr:
        s += zahl
    return s

def produkt(arr):
    p = 1
    for zahl in arr:
        p *= zahl
    return p

def doppel(arr):
    res = []
    for zahl in arr:
        res += [zahl, -zahl]
    return res

if len(sys.argv) < 3:
    print("Es fehlen Parameter.")
else:
    zahlen = []
    
    try:
        for p in sys.argv[1:-1]:
            zahlen += [float(p)]
    except:
        print("Ungültige Zahl eingegeben.")
    else:
        op = sys.argv[-1]
        
        if op == "s":
            print(summe(zahlen))
        elif op == "m":
            print(produkt(zahlen))
        elif op == "d":
            print(doppel(zahlen))
        else:
            print("Keine gültige Operation angegeben.")
