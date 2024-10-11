# a = qa*k + m
# b = qb*k + n
# a + b = (qa + qb)*k + m + n

from math import gcd

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def maximize_mex(base, n, k):
	ini, fin = k - 1, n + k - 1
	if fin - k + 1 <= (fin - 1)//base + 1:
		return fin

	while ini + 1 != fin:
		middle = (ini + fin)//2
		if middle - k + 1 <= (middle - 1)//base + 1:
			ini = middle
		else:
			fin = middle
	return ini

t = int(input())

for _ in range(t):
	n, k = read_line()
	a = read_line()
	if len(a) == 1:
		print(k if a[0] < k else k - 1)
		continue

	base = a[0]
	for el in a:
		base = gcd(base, el)
	print(maximize_mex(base, n, k))

