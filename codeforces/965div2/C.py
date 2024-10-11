# length odd
# . o . . o

# length even
# . . o . . o
# 1 1 2 5

# n//2 - 1 and n - 1

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def reorder(a, b):
	ab = [[a[idx], b[idx]] for idx in range(len(a))]
	ab.sort()
	return [el[0] for el in ab], [el[1] for el in ab]

def last_strategy(a, b, k):
	one = -1
	for idx in range(n):
		if b[idx] == 1:
			one = idx
	if one == -1 or a[one] + k < a[n - 1]:
		return a[n//2 - 1] + a[n - 1]
	if one <= n//2 - 1:
		return a[n//2] + a[one] + k
	else:
		return a[n//2 - 1] + a[one] + k

def compute_costs(a, b):
	ini, fin = len(a)//2 - 2, len(a)//2 - 1
	costs = [10**9]*len(a)
	for idx in range(len(b)):
		if b[idx] == 1:
			costs[idx] = 0
	while ini >= 0 and fin < len(a):
		while ini >= 0 and b[ini] == 0:
			ini -= 1
		while fin < len(a) and b[fin] == 1:
			fin += 1
		if ini >= 0 and fin < len(a):
			costs[fin] = a[fin] - a[ini]
			fin += 1
			ini -= 1
	return costs

def middle_strategy(a, b, k):
	ops, middle_idx = 0, len(a)//2 - 1
	costs = compute_costs(a, b)
	while middle_idx + 1 < len(a):
		ops += costs[middle_idx]
		if ops >= k: return a[middle_idx] + a[-1]
		if ops + (a[middle_idx + 1] - a[middle_idx])*(middle_idx - len(a)//2 + 2) > k: break
		ops += (a[middle_idx + 1] - a[middle_idx])*(middle_idx - len(a)//2 + 2)
		middle_idx += 1
	if middle_idx + 1 == len(a):
		return a[middle_idx] + a[-1]
	return a[middle_idx] + (k - ops)//(middle_idx - len(a)//2 + 2) + a[-1]

t = int(input())

for _ in range(t):
	n, k = read_line()
	a = read_line()
	b = read_line()
	a, b = reorder(a, b)
	print(max(last_strategy(a, b, k), middle_strategy(a, b, k)))

