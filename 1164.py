c = int(input())
for a in range(0,c):
	x = int(input())
	v = []
	for b in range(1,x):
		if x % b == 0:
			v.append(b)
	if sum(v) == x:
		print("%d eh perfeito"% x)
		v = []
	else:
		print("%d nao eh perfeito"% x)
		v = []		