def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def median(a):
	return a[len(a)//2]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()
	if len(a) < 3:
		print(-1)
		continue

	a.sort()
	print(max(median(a)*len(a)*2 - sum(a) + 1, 0))

