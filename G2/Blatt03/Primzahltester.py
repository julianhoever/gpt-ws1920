import sys

zahl = int(sys.argv[1])

if zahl >= 2:
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            print("False")
            break
    else:
        print("True")
else:
    print("False")
