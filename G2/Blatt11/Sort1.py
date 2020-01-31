def tausche(l,a,b):
	t = l[a]
	l[a] = l[b]
	l[b] = t

def sort1(liste):
	le = len(liste)
	for i in range(0,le//2):
		mi = i
		ma = i
		for j in range(i+1,le-i):
			if liste[j] < liste[mi]: mi = j
			elif liste[j] > liste[ma]: ma = j
			
		tausche(liste,i,mi)
		if i==ma: ma = mi
		tausche(liste,(le-i)-1,ma)