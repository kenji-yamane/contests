def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n, m, k = read_line()
	ans = []
	for idx in range(n, m, -1):
		ans.append(idx)
	for idx in range(1, m + 1):
		ans.append(idx)
	print(*ans)

