def read_line():
	x = input().strip().split(' ')
	return [int(i) for i in x]

def stabilize_point(matrix, i, j):
	max_neighbor = 1
	for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
		if 0 <= i + d[0] < len(matrix) and 0 <= j + d[1] < len(matrix[0]):
			max_neighbor = max(max_neighbor, matrix[i + d[0]][j + d[1]])
	matrix[i][j] = min(matrix[i][j], max_neighbor)

t = int(input())

for _ in range(t):
	n, m = read_line()
	matrix = []
	for _ in range(n):
		row = read_line()
		matrix.append(row)

	for i in range(n):
		for j in range(m):
			stabilize_point(matrix, i, j)
	for row in matrix:
		print(*row)

