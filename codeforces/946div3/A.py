# o o o
# o o o
# o o o
# o o o
# o o o

def ceil(x, div):
	if x%div == 0:
		return x//div
	else:
		return x//div + 1

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	x, y = read_line()

	ans = ceil(y, 2)
	cells_left = ans*5*3 - 2*2*y
	ans += ceil(max(x - cells_left, 0), 5*3)
	print(ans)

