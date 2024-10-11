def read_numbers():
	line = input().strip().split(' ')
	line = [int(i) for i in line]
	return line

def ceil(x, y):
	return x//y if x%y == 0 else x//y + 1

def log2(x):
	ans = 0
	y = 1
	while y < x:
		y <<= 1
		ans += 1
	return ans

def try_match(ini, x, s):
	for i in range(len(s)):
		if x[ini] != s[i]:
			return False
		ini = (ini + 1)%len(x)
	return True

def fit(x, s):
	for ini in range(len(x)):
		if try_match(ini, x, s):
			return log2(ceil(len(s) + ini, len(x)))
	return -1

t = int(input())

for _ in range(t):
	n, m = read_numbers()
	x = input().strip()
	s = input().strip()

	print(fit(x, s))

