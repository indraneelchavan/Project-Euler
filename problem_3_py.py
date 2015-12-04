import math

n = 600851475143
factors = []

while n % 2 == 0:
    factors.append(2)
    n = n / 2

number = int(math.ceil((math.sqrt(n))))

if n == 3:
    factors.append(3)
    n = n / 3
else:
    for i in range(3, number):
        while n % i == 0:
            factors.append(i)
            n = n / i

if len(factors) == 0:
    factors.append(1)
    factors.append(n)
elif len(factors)!= 0 and n!= 1 :
    factors.append(n)

print factors
print max(factors)