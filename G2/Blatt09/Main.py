import sys
import Fibonacci
import Summe

if len(sys.argv) > 1:
    zahl = int(sys.argv[1])
    print(Fibonacci.fibonacci(zahl))
else:
    print(Summe.summe())
