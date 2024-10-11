t = int(input())

for _ in range(t):
	nkx = input().strip().split(' ')
	n, k, x = [int(i) for i in nkx]
	if (1 + k)*k//2 <= x <= (n - k + 1 + n)*k//2:
		print('YES')
	else:
		print('NO')
