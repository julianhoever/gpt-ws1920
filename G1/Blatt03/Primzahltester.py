import sys

zahl = int(sys.argv[1])

if zahl < 2:
    print("False")
else:
    for i in range(2, zahl:
        if zahl % i == 0:
            print("False")
            break
    else:    
        print("True")
