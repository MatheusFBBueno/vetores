d = 0
c = int(input())
for o in range(0,c):
	x = int(input())
	if x == 1 or x == 2:
		print("%d eh primo"% x)
	else:
		for a in range(2,x):
			if x % a == 0:
				d += 1
		if d > 0:
			print("%d nao eh primo"% x)
			d = 0
		else:
			print("%d eh primo"%x)
			d = 0