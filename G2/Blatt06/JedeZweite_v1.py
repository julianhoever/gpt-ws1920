import sys

# zeilen = []
# for zeile in sys.stdin:
#     zeilen += [zeile]

zeilen      = sys.stdin.readlines()   
jede_zweite = zeilen[1::2]

sys.stdout.writelines(jede_zweite)
