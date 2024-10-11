# layer 1 -> root
# layer 2 -> identified in the n - 1 scan -> 1 time
# layer 3 -> mapped to layer 2 in n - 1 scan -> 2 times
# layer 4 -> mapped to layer 2 in n - 1 scan -> 2 times
# layer 5 -> mapped to layer 3 in n - 1 scan -> 2 times
# layer 6 -> mapped to layer 3 in n - 1 scan -> 3 times
# layer 7 -> mapped to layer 4 in n - 1 scan -> 3 times
# layer 8 -> mapped to layer 4 in n - 1 scan -> 3 times

from sys import stdout

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def query(a, b):
	print('?', a + 1, b + 1)
	stdout.flush()
	return int(input()) - 1

t = int(input())

for _ in range(t):
	n = int(input())

	parents = [-1]*n
	parents[0] = 0
	for i in range(1, n):
		parent = 0
		middle = query(parent, i)
		while middle != parent:
			parent = middle
			middle = query(parent, i)
		parents[i] = parent

	ans = []
	for i in range(1, n):
		ans.append(parents[i] + 1)
		ans.append(i + 1)
	print('!', *ans)

