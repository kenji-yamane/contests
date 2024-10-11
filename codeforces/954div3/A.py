def read_line():
	x = input().strip().split(' ')
	return [int(i) for i in x]

t = int(input())

for _ in range(t):
	x = read_line()
	x.sort()
	print(x[2] - x[0])

