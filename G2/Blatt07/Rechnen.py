import sys

def durchschnitt(arr):
    return sum(arr)/len(arr)

def minimum(arr):
    min_i = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_i]:
            min_i = i
    return arr[min_i]

def minimum2(arr):
    mini = arr[0]
    for element in arr:
        if element < mini:
            mini = element
    return mini

def maximum(arr):
    max_i = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_i]:
            max_i = i
    return arr[max_i]

zahlen = []
for zahl in sys.stdin:
    zahlen += [float(zahl)]
    
print("Durchschnitt:", durchschnitt(zahlen))
print("Minimum:", minimum(zahlen))
print("Maximum:", maximum(zahlen))
