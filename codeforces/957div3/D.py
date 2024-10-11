def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n, m, k = read_line()
	river = input().strip()

	optimal_swim = [3*10**5]*(n + 1)
	for i in range(m):
		if i < n and river[i] == 'C':
			continue
		if i <= n:
			optimal_swim[i] = 0

	for i in range(n):
		if river[i] == 'C':
			continue
		if river[i] == 'W':
			if i + 1 < n and river[i + 1] == 'C':
				continue
			optimal_swim[i + 1] = min(optimal_swim[i + 1], optimal_swim[i] + 1)
			continue
		if river[i] == 'L':
			for j in range(m):
				dest = i + j + 1
				if dest < n and river[dest] == 'C':
					continue
				if dest <= n:
					optimal_swim[dest] = min(optimal_swim[dest], optimal_swim[i])

	if optimal_swim[-1] <= k:
		print('yes')
	else:
		print('no')

