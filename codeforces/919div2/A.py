t = int(input())

for _ in range(t):
	n = int(input())
	lowers, uppers, unequals = [], [], []
	for _ in range(n):
		a, x = input().strip().split(' ')
		a, x = int(a), int(x)
		if a == 1:
			lowers.append(x)
		elif a == 2:
			uppers.append(x)
		else:
			unequals.append(x)
	lower, upper = max(lowers), min(uppers)
	if upper < lower:
		print(0)
		continue

	ans = upper - lower + 1
	for unequal in unequals:
		if lower <= unequal <= upper:
			ans -= 1
	print(ans)
