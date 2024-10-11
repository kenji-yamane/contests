# 10 2 5 2 7 9 2 5 10 7
# 10 5 2 7 9 2 5 10 7
# 7
# 1 2 3 4

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()
	a.sort()
	print(a[len(a)//2])

