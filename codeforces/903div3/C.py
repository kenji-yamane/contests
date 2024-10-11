def read_numbers():
	line = input().strip().split(' ')
	line = [int(i) for i in line]
	return line

def idx2cart(n, i, j):
	return -(2*i - n + 1), 2*j - n + 1

def cart2idx(n, x, y):
	return (-x - 1 + n)//2, (y - 1 + n)//2

def rotate90(x, y):
	return -y, x

def fix_cycle(matrix, i, j):
	cycle = [matrix[i][j]]
	x, y = idx2cart(len(matrix), i, j)
	for _ in range(3):
		x, y = rotate90(x, y)
		i, j = cart2idx(len(matrix), x, y)
		cycle.append(matrix[i][j])
	return sum([ord(max(cycle)) - ord(let) for let in cycle])

t = int(input())

for _ in range(t):
	n = int(input())
	matrix = []
	for _ in range(n):
		matrix.append(input().strip())
	ans = 0
	for i in range(n//2):
		for j in range(n//2):
			ans += fix_cycle(matrix, i, j)
	print(ans)

