def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	a, b, c = read_line()

	ans = a*b*c
	for i in range(6):
		for j in range(6):
			for k in range(6):
				if i + j + k <= 5:
					ans = max(ans, (a + i)*(b + j)*(c + k))
	print(ans)

