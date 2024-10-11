def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

t = int(input())

for _ in range(t):
	n, f, k = read_line()
	a = read_line()

	favorite = a[f - 1]
	a.sort(reverse=True)
	first, last = -1, -1
	for idx, el in enumerate(a):
		if el == favorite:
			first = idx
			break
	for idx, el in enumerate(reversed(a)):
		if el == favorite:
			last = n - idx - 1
			break

	if k - 1 < first:
		print('no')
	elif k - 1 >= last:
		print('yes')
	else:
		print('maybe')

