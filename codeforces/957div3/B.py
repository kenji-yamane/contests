def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n, k = read_line()

	a = read_line()

	greatest = max(a)
	num_greatest = 0
	ans = 0
	for el in a:
		if el < greatest:
			ans += el - 1
			ans += el
		else:
			num_greatest += 1
	ans += (num_greatest - 1)*(greatest - 1)
	ans += (num_greatest - 1)*greatest
	print(ans)

