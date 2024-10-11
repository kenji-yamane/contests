from math import gcd

def read_array():
	arr = input().strip().split(' ')
	arr = [int(i) for i in arr]
	return arr

def sieve(n):
	is_prime = [True]*(n + 1)
	is_prime[0] = is_prime[1] = False
	for i in range(2, n + 1):
		j = 2
		while i*j <= n:
			is_prime[i*j] = False
			j += 1

	primes = []
	for i in range(n + 1):
		if is_prime[i]:
			primes.append(i)
	return primes, is_prime

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_array()
	primes, is_prime = sieve(n)

	prime_divisors = list(filter(lambda prime : n%prime == 0, primes))
	powers = [0]*len(prime_divisors)
	for idx, prime in enumerate(prime_divisors):
		copy_n = n
		while copy_n%prime == 0:
			copy_n /= prime
			powers[idx] += 1

	if n == 1:
		print(1)
		continue
	candidates = -1
	for idx in range(len(a) - 1):
		diff = abs(a[idx + 1] - a[idx])
		if diff > 0:
			if candidates == -1:
				candidates = diff
			candidates = gcd(candidates, diff)
	if candidates > 1 or candidates == -1:
		ans = 1
		for power in powers:
			ans *= power + 1
		print(ans)
		continue

	points = [False]*len(prime_divisors)
	for idx, divisor in enumerate(prime_divisors):
		candidates = -1
		for i in range(divisor):
			for j in range(n//divisor - 1):
				diff = abs(a[(j + 1)*divisor + i] - a[j*divisor + i])
				if diff > 0:
					if candidates == -1:
						candidates = diff
					candidates = gcd(candidates, diff)
		if candidates > 1 or candidates == -1:
			points[idx] = True

	ans = 1
	perfect_score = True
	for idx in range(len(points)):
		if points[idx]:
			ans *= powers[idx] + 1
		else:
			perfect_score = False
	print(ans - 1 if perfect_score else ans)
