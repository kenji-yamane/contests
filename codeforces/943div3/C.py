# a1 = x2 + 1

# ai%aprevious = xi
# ai = aprevious*k + xi, xi < k
# ai = aprevious*(xi + 1) + xi
# ai = aprevious + xi
# ai = mcm(aprevious, xi + 1) + xi
# ai = aprevious*x
# ai = aprevious//gcd(aprevious, xi + 1)
# ai = xi + 1 + xi

# ai = q*(xi + 1) + xi

# an, xn
# an%aprevious = xn
# an = aprevious*k + xn
# aprevious = (an - xn)//k

def read_line():
	line = input().strip().split(' ')
	line = [int(i) for i in line]
	return line

t = int(input())

for _ in range(t):
	n = int(input())
	x = read_line()
	a = [501]

	for el in x:
		a.append(a[-1] + el)
	print(*a)

