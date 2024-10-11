# ab + ac + bc <= n
# x    y    z
# b = az/y
# c = by/x
# a = cx/z
# a**2 = xy/z
# b**2 = zx/y
# c**2 = zy/x
# (a*b*c)**2 = xyz
# xyz <= n**3

# a**2 + b**2 + c**2 + b(a + c) + a(b + c) + c(a + b) <= x**2
# a**2 bc <= n**2

# a**2 + b**2 + c**2 <= 3x**2
# (a + b + c)**2 <= 3x**2 + 2*n

# b(a + 1) + a(c + 1) + c(b + 1) <= n + x
# a(1 + b + c) + b + c + bc + 1 <= n + x + 1
# (a + 1)(1 + b + c) + bc <= n + x + 1

# xyz = q = (abc)**2
# x + y + z <= n
# a + b + c <= x

# a + b <= x - c
# ab + c(a + b) <= n
# ab <= n - c(a + b)
# ab <= n - cs
# a(s - a) <= n - cs
# s - 1 <= n - cs
# s <= (n + 1)//(c + 1)
# s <= (n + a**2)//(c + a)

# s**2 <= 4n - 4cs
# s**2 + 4cs - 4n <= 0
# s = -2c + 2sqrt(c**2 + n)
# 2c**2 + n - 2csqrt(c**2 + n)

# c(a + b) <= n
# a + b <= n//c

# -2c + 2sqrt(c**2 + n) <= n/c

# a(c + b) + cb <= n
# a(c + b) + cb + c**2 <= n + c**2
# a(c + b) + c(c + b) <= n + c**2
# (c + a)(c + b) <= n + c**2
# c + b <= (n + c**2)//(c + a)

# c + a <= x - b

# ab <= n
# n + n//2 + n//3 + n//4

# s + c <= x
# sc <= n - ab
# c <= (n - ab)//s
# (n - s)//s
# (n - s**2/4)//s

# b(s - b) + as = n
# b**2 - sb + n - as = 0
# b = (s - sqrt(s**2 - 4n + 4as))/2
# s - sqrt(s**2 - 4n + 4as)
# s**2 - 2ks + k**2 = s**2 - 4n + 4as
# s = (4n + k**2)//(2k + 4a)

# bc + a(b + c) <= n
# start: 2
# middle: floor(-2c + 2sqrt(c**2 + n))
# end: min(n//a, x - a)
# bc <= n - a(b + c)
# n - a(b + c) = 1 => b + c = (n - 1)//a
# (b + c) <= (n - k)//a
# b + c <= x - a

# a <= x - s
# a <= (n - bc)//s

# a <= n
# b <= n//a
# c <= min((n - ab)//(a + b), x - a - b)

# n - a*b >= a + b
# b <= (n - a)//(a + 1)
# n - a*b >= (a + b)*k
# n - a*b >= a*k + b*k
# b <= (n - a*k)//(a + k)
# (n - a**2)/a
# n - 1 + (n - 4)/2 + (n - 9)/3
# n + n/2 + n/3 + ... + sqrt(n)
# 1 + 2 + ... + sqrt(n)

# x - a - b >= b
# b <= (x - a)//2
# (n - a*b)/(a + b) >= b
# ab + b**2 <= n - ab
# b**2 + 2ab - n <= 0
# b = -a + sqrt(a**2 + n)

from math import sqrt as math_sqrt, ceil

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def permutations(a, b, c): # a <= b <= c
	if a == b == c:
		return 1
	elif b == c:
		return 3
	elif a == b:
		return 3*(c - b) + 1
	else:
		return 6*(c - b) + 3

def sqrt(n):
	ans = 0
	while ans*ans < n:
		ans += 1
	return ans

t = int(input())

for _ in range(t):
	n, x = read_line()
	root_n = sqrt(n)

	ans = 0
	for a in range(1, root_n):
		for b in range(a, min(ceil(-a + math_sqrt(a**2 + n)) + 1, (x - a)//2 + 1)):
			max_c = min((n - a*b)//(a + b), x - a - b)
			if max_c < b:
				continue
			ans += permutations(a, b, max_c)
	print(ans)

