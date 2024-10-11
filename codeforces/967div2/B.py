from collections import deque

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	if n%2 == 0:
		print(-1)
		continue

	ans = deque()
	ans.append(1)
	curr = 2
	for i in range((n - 1)//2):
		ans.append(curr)
		curr += 1
		ans.appendleft(curr)
		curr += 1
	print(*ans)

