import sys

start = int(sys.argv[1])
ende  = int(sys.argv[2])

for i in range(start, ende + 1):
    print("\t" + str(i), end="")
print()

for i in range(start, ende + 1):
    print(i, end="\t")
    
    for j in range(start, ende + 1):
        print(i*j, end="\t")
        
    print()
