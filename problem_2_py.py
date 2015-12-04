fib_list = [1];
fib_num = 1
even_total = 0
i = 0

while fib_num < 4000000:
    fib_list.append(fib_num)
    i += 1
    fib_num = fib_list[i] + fib_list[i-1]

for j in fib_list:
    if j % 2 == 0:
        even_total += j

print even_total