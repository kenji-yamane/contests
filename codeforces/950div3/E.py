def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

def transpose(mtx):
	transposed = [[] for i in range(len(mtx[0]))]
	for row in mtx:
		for idx, el in enumerate(row):
			transposed[idx].append(el)
	return transposed

def rowwise_equal(a, b):
	for row in a:
		row.append(min(row))
	for row in b:
		row.append(min(row))
	a.sort(key=lambda x : x[-1])
	b.sort(key=lambda x : x[-1])
	for idx in range(len(a)):
		if set(a[idx]) != set(b[idx]):
			return False
	return True

t = int(input())

for _ in range(t):
	n, m = read_line()

	a = []
	for _ in range(n):
		a.append(read_line())
	at = transpose(a)

	b = []
	for _ in range(n):
		b.append(read_line())
	bt = transpose(b)

	if rowwise_equal(a, b) and rowwise_equal(at, bt):
		print('yes')
	else:
		print('no')

