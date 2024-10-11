def read_line():
	line = input().strip().split(' ')
	line = [int(i) for i in line]
	return line

t = int(input())

for _ in range(t):
	n = int(input())

	ans = [[1, 1], [n, n]]
	if n > 2:
		ans.append([n - 1, n])
	for i in range(3, n):
		ans.append([1, i])
	for el in ans:
		print(*el)

