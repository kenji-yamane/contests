def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	a, b = read_line()
	total_sum = a*1 + b*2
	if total_sum%2 == 1:
		print('NO')
		continue

	found = False
	for ai in range(a + 1):
		for bi in range(b + 1):
			if ai + 2*bi == total_sum//2:
				found = True
	if found:
		print('YES')
	else:
		print('NO')

