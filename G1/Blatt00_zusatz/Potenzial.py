import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

p1 = a ** b
p2 = b ** a

vergleich = p1 == p2

print(a, "hoch", b, "=", p1)
print(b, "hoch", a, "=", p2)
print()
print("Sind die beiden Potenzen gleich:", vergleich)
