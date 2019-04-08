i = 0
for _ in range(0,10):
	x = int(input())
	if x <= 0:
		print("X[%d] = 1"%i)
		i += 1
	else:
		print("X[%d] = %d"% (i,x))
		i += 1