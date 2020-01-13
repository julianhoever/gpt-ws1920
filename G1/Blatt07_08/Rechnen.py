import sys

def durchschnitt(arr):
    return sum(arr)/len(arr)

def minimum(arr):
    curr_min = arr[0]
    
    for ele in arr:
        if ele < curr_min:
            curr_min = ele
    
    return curr_min

def maximum(arr):
    curr_max = arr[0]
    
    for ele in arr:
        if ele > curr_max:
            curr_max = ele
    
    return curr_max


zahlen = []
for zeile in sys.stdin:
    zahlen += [float(zeile)]
    
print("Durchschnitt:", durchschnitt(zahlen))
print("Minimum:", minimum(zahlen))
print("Maximum:", maximum(zahlen))
