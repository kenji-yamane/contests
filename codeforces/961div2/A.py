def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

t = int(input())

for _ in range(t):
	n, k = read_line()
	if k == 0:
		print(0)
		continue

	ans = 1
	k -= n
	n -= 1
	while k > 0:
		k -= n
		ans += 1
		if k <= 0:
			break
		k -= n
		ans += 1
		n -= 1
	print(ans)

