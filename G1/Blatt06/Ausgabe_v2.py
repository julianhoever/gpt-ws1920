import sys

with open("Ausgabe_v2.py", "r") as datei:
    sys.stdout.writelines(datei.readlines())
