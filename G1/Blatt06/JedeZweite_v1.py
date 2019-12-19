import sys

zeilen      = sys.stdin.readlines()
jede_zweite = zeilen[1::2]

sys.stdout.writelines(jede_zweite)
