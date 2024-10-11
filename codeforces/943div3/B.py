from math import gcd

def read_numbers():
	line = input().strip().split(' ')
	line = [int(i) for i in line]
	return line

t = int(input())

for _ in range(t):
	n, m = read_numbers()
	a = input().strip()
	b = input().strip()

	ia, ib = 0, 0
	while ia < len(a) and ib < len(b):
		if a[ia] == b[ib]:
			ia += 1
			ib += 1
		else:
			ib += 1
	print(ia)

