def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def shift(arr):
	ans = []
	for i in range(1, len(arr)):
		ans.append(arr[i])
	ans.append(arr[0])
	return ans

t = int(input())

for _ in range(t):
	n = int(input())
	p = read_line()
	print(*shift(p))

