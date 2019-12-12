# Imports
import sys

# Funktionsdefinitionen
def add(x, y):
    return x + y

def diff(x, y):
    return abs(x - y)

def mul(x, y):
    # abs(-3) * -5
    if x < 0:
        x = abs(x)
        y = -y
    
    ergebnis = 0
    for i in range(0, x):
        ergebnis += y
        
    return ergebnis

def div(x, y):
    return x / y


# Hauptprogramm
print("Addition: ", add(int(sys.argv[1]), int(sys.argv[2])))
print("Differenz: ", diff(int(sys.argv[1]), int(sys.argv[2])))
print("Multiplikation: ", mul(int(sys.argv[1]), int(sys.argv[2])))
print("Division: ", div(int(sys.argv[1]), int(sys.argv[2])))
