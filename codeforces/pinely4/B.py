# a0 and a1 contains at least the b0 bits
# a1 contains at least the b1 bits
# a0 = b0
# a1 = b0 | b1
# a1 & a0 = b0
# a1 & a2 = b1
# a_(n + 1) = bn

# 1 2 3
# 1 3 3

# 1
# 1 1

# 2 0
# 2 2 0

# 3 5 4 2
# 3 (11) 7 (111) 5 (101) 6 (110) 2

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	b = read_line()

	a = [b[0]]
	for idx in range(1, len(b)):
		a.append(b[idx] | b[idx - 1])
	a.append(b[-1])

	valid = True
	for idx in range(1, len(a)):
		if b[idx - 1] != (a[idx] & a[idx - 1]):
			valid = False
	if valid:
		print(*a)
	else:
		print(-1)

