import sys

n = int(sys.argv[1])
summe = "1"
ergebnis = 1

for i in range(2, n+1):
    summe += " + " + str(i)
    ergebnis += i

print(summe, "=", ergebnis)
