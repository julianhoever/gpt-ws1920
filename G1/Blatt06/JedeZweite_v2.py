import sys

zeilen = sys.stdin.readlines()

for i in range(1, len(zeilen), 2):
    print(zeilen[i], end="")
