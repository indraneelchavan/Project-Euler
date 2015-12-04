sum = 0
a, b = 1, 0
while a < 4*10**6:
	a, b = a + b, a
	if a % 2 == 0:
		sum += a
print (sum)
