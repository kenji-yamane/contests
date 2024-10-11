def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	xc, yc, k = read_line()

	if k%2 == 1:
		print(xc, yc)
	for i in range(k//2):
		print(xc + i + 1, yc + i + 1)
		print(xc - i - 1, yc - i - 1)

