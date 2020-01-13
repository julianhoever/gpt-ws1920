import sys

def quersumme(n):
    qs = 0
    while n != 0:
        qs += n % 10
        n //= 10
    return qs

def istPrimzahl(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def primfaktoren(n):
    if istPrimzahl(n):
        return [n]
    
    faktoren = []
    i = 2
    while n > 1:
        if n % i == 0:
            faktoren += [i]
            n //= i
        else:
            i += 1
    
    return faktoren

def istPerfekt(n):
    summe = 0
    for i in range(1, n):
        if n % i == 0:
            summe += i
            
    return summe == n

zahl = int(sys.argv[1])
print("Quersumme:", quersumme(zahl))
print("Primfaktoren:", primfaktoren(zahl))
print("Ist perfekt:", istPerfekt(zahl))
