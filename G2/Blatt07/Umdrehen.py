import sys

zeilen = []

try:
    with open(sys.argv[1], "r") as datei:
        zeilen = datei.readlines()

except:
    print("Datei ist nicht vorhanden oder kann nicht geoeffnet werden.")

else:
    # zeilen = zeilen[::-1]
    # 
    # for zeile in zeilen:
    #     print(zeile[::-1], end="")
    
    for i in range(len(zeilen)-1, -1, -1):
        for c in range(len(zeilen[i])-1, -1, -1):
            print(zeilen[i][c], end="")
