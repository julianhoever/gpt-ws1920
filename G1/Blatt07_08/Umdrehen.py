import sys

zeilen = []

try:
    with open(sys.argv[1], "r") as quelldatei:
        zeilen = quelldatei.readlines()
except:
    print("Fehler beim lesen der Datei.")
else:
    zeilen = zeilen[::-1]
    
    for zeile in zeilen:
        print(zeile[::-1], end="")
