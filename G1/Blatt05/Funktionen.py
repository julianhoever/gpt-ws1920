import sys

def add(x, y):
    return x + y

# def diff(x, y):
#     betrag = x - y
#     if betrag < 0:
#         betrag = -betrag
#     return betrag

def diff(x, y):
    return abs(x - y)

def mul(x, y):
    if y < 0:
        y = abs(y)
        x = -x
    
    prod = 0
    for i in range(0, y):
        prod += x
    return prod

def div(x, y):
    return x / y


a = int(sys.argv[1])
b = int(sys.argv[2])

print(add(a, b))
print(diff(a,b))
print(mul(a,b))
if b != 0:
    print(div(a,b))
else:
    print("Division durch 0 nicht erlaubt")
