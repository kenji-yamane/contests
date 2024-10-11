# a*n - b
# n*(10**(n//10 + 1)**a - 1)/9//10**b
# n*(10**a - 1)/9 + b

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def digits(x):
	ans = 0
	while x > 0:
		x //= 10
		ans += 1
	return ans

def answer_for_one(max_a):
	ans = []
	for b in range(1, max_a):
		ans.append((b + 1, b))
	print(len(ans))
	for el in ans:
		print(*el)

t = int(input())

for _ in range(t):
	n = int(input())
	max_a = 10**4
	if n == 1:
		answer_for_one(max_a)
		continue

	x = n
	while x < max_a*n:
		x *= 10**digits(n)
		x += n

	ans = []
	while x > 0:
		x //= 10
		if x <= 0 or x >= max_a*n:
			continue
		dividend = x*digits(n) - digits(x)*n
		divisor = n - digits(n)
		if dividend*divisor <= 0 or dividend%divisor != 0:
			continue

		b = dividend//divisor
		if (x + b)%n != 0:
			continue
		a = (x + b)//n
		if 1 <= a <= max_a and 1 <= b <= min(max_a, a*n):
			ans.append((a, b))
	ans.sort()
	print(len(ans))
	for el in ans:
		print(*el)

