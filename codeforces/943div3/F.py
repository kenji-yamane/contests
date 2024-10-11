from bisect import bisect_left

def read_line():
	line = input().strip().split(' ')
	line = [int(i) for i in line]
	return line

def get_cum_xor(arr):
	ans = []
	xor_so_far = 0
	for el in arr:
		xor_so_far ^= el
		ans.append(xor_so_far)
	return ans

def get_freqs(arr):
	ans = {}
	for idx, el in enumerate(arr):
		if el not in ans:
			ans[el] = []
		ans[el].append(idx)
	rev_ans = {}
	for key, value in ans.items():
		rev_ans[key] = value.copy()
		rev_ans[key].reverse()
	return ans, rev_ans

t = int(input())

for ti in range(t):
	n, q = read_line()
	a = read_line()
	cum_xor = get_cum_xor(a)
	cum_freqs, rev_cum_freqs = get_freqs(cum_xor)

	for i in range(q):
		l, r = read_line()
		l -= 1
		r -= 1

		left_cum = 0
		if l > 0:
			left_cum = cum_xor[l - 1]
		lr_xor = cum_xor[r] ^ left_cum
		if lr_xor == 0:
			print('yes')
			continue

		right_zero = bisect_left(cum_freqs[cum_xor[r]], l)
		if left_cum not in rev_cum_freqs:
			print('no')
			continue
		left_zero = bisect_left(rev_cum_freqs[left_cum], -r, key = lambda x : -x)
		if left_zero == len(rev_cum_freqs[left_cum]):
			print('no')
			continue

		if cum_freqs[cum_xor[r]][right_zero] < rev_cum_freqs[left_cum][left_zero]:
			print('yes')
		else:
			print('no')

	if ti < t - 1:
		print()

