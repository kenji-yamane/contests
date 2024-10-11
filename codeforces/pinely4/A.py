def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	ans = a[0]
	for i in range(0, n, 2):
		ans = max(ans, a[i])
	print(ans)

