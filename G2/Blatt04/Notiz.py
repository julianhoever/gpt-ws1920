import sys

with open("Notiz.txt", "w") as out:
    for zeile in sys.stdin:
        out.write(zeile)
