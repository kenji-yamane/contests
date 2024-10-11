def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n, k = read_line()

	grid = []
	for _ in range(n):
		grid.append(input().strip())

	reduced_grid = []
	for i in range(n//k):
		row = []
		for j in range(n//k):
			row.append(grid[i*k][j*k])
		reduced_grid.append(row)

	for row in reduced_grid:
		print(''.join(row))

