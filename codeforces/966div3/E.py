def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n, m, k = read_line()
	w = int(input())
	a = read_line()

	weights = []
	for i in range(n):
		for j in range(m):
			hor = min(i, n - k) - max(i - k + 1, 0) + 1
			ver = min(j, m - k) - max(j - k + 1, 0) + 1
			weights.append(hor*ver)
	weights.sort(reverse=True)
	a.sort(reverse=True)
	spectacle = 0
	for idx, el in enumerate(a):
		spectacle += el*weights[idx]
	print(spectacle)

