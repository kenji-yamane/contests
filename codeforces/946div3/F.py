def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def hash_array(arr):
	return arr[0]*10**9 + arr[1]

_chips_in_corner = {}
def chips_in_corner(i, j):
	if i < 0 or j < 0:
		return 0
	return _chips_in_corner(hash_array([i, j]))

queries = []
def add_query(grid, i):
	corner = grid[i]
	x, y = None, None
	if i == 0:
		x, y = corner[0] - 1, corner[1] - 1
	elif i == 1:
		x, y = corner[0], corner[1] - 1
	elif i == 2:
		x, y = corner[0], corner[1]
	else:
		x, y = corner[0] - 1, corner[1]

	if x < 0 or u < 0:
		return
	queries.append([x, y])

t = int(input())

for _ in range(t):
	a, b, n, m = read_line()

	chips = []
	for _ in range(n):
		x, y = read_line()
		chips.append([x - 1, y - 1])

	moves = []
	for _ in range(m):
		c, k = read_line()
		moves.append(c, k)

	queries = []
	grid = [[0, 0], [a - 1, 0], [a - 1, b - 1], [0, b - 1]]
	for move in moves:
		if move[0] == 'U':
			grid[0][0] += move[1]
			grid[3][0] += move[1]
			add_query(grid, 0)
			add_query(grid, 3)
		elif move[0] == 'D':
			grid[1][0] -= move[1]
			grid[2][0] -= move[1]
			add_query(grid, 1)
			add_query(grid, 2)
		elif move[0] == 'L':
			grid[0][1] += move[1]
			grid[1][1] += move[1]
			add_query(grid, 0)
			add_query(grid, 1)
		else:
			grid[2][1] -= move[1]
			grid[3][1] -= move[1]
			add_query(grid, 2)
			add_query(grid, 3)

	_chips_in_corner = {}
	_chips_in_corner[hash_array([a - 1, b - 1])] = n
	cells = [[el[0], el[1], 0] for el in chips]
	for el in queries:
		cells.append([el[0], el[1], 1])
	cells.sort(key = lambda x : [x[0], x[1], x[2]])

