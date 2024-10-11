def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	total_sum = sum(a)
	ans = 0
	for el in a:
		ans += (total_sum - el)*el
		ans %= 10**9 + 7
	denominator = pow((n*(n - 1))%(10**9 + 7), -1, 10**9 + 7)
	print(ans*denominator%(10**9 + 7))

