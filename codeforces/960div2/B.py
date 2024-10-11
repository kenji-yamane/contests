from collections import deque

def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

t = int(input())

for _ in range(t):
	n, x, y = read_line()
	ans = deque()
	for i in range(x - y + 1):
		ans.append(1)
	curr = -1
	for i in range(x + 1, n + 1):
		ans.append(curr)
		curr *= -1
	curr = -1
	for i in range(1, y):
		ans.appendleft(curr)
		curr *= -1
	print(*ans)

