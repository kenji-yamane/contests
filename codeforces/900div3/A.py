t = int(input())

for _ in range(t):
	nk = input().strip().split(' ')
	n, k = [int(i) for i in nk]
	a = input().strip().split(' ')
	a = [int(i) for i in a]
	if k in a:
		print('YES')
	else:
		print('NO')
