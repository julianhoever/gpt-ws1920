import sys

n = int(sys.argv[1])
rechnung = "1"
ergebnis = 1

for i in range(2, n+1):
    rechnung += " + " + str(i)
    ergebnis += i
    
print(rechnung, "=", ergebnis)
