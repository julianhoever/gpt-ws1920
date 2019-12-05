import sys

with open("Notiz.txt", "w") as file:
    for zeile in sys.stdin:
        file.write(zeile)
