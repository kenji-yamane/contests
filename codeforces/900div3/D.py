t = int(input())

for _ in range(t):
	nk = input().strip().split(' ')
	n, k = [int(i) for i in nk]
	s = input().strip()
	l = input().strip().split(' ')
	l = [int(i) for i in l]
	r = input().strip().split(' ')
	r = [int(i) for i in r]
	q = int(input())
	x = input().strip().split(' ')
	x = [int(i) for i in x]

	unilateral_reversals = [False]*n
	for el in x:
		unilateral_reversals[el - 1] = not unilateral_reversals[el - 1]

	reversals = [False]*n
	seg_idx = 0
	for i in range(n):
		if i + 1 > r[seg_idx]:
			seg_idx += 1
		if not unilateral_reversals[i]:
			continue
		xi = i + 1
		mirror_xi = r[seg_idx] + l[seg_idx] - xi
		ini, fin = min(xi, mirror_xi) - 1, max(xi, mirror_xi) - 1
		reversals[ini] = not reversals[ini]
		reversals[fin] = not reversals[fin]

	seg_idx = 0
	is_reversed = False
	ans = []
	for i in range(n):
		if i + 1 > r[seg_idx]:
			seg_idx += 1
		if reversals[i] and i + 1 == min(i + 1, r[seg_idx] + l[seg_idx] - i - 1):
			is_reversed = not is_reversed
		if not is_reversed:
			ans.append(s[i])
		else:
			ans.append(s[r[seg_idx] + l[seg_idx] - i - 1 - 1])
		if reversals[i] and i + 1 == max(i + 1, r[seg_idx] + l[seg_idx] - i - 1):
			is_reversed = not is_reversed
	print(''.join(ans))

