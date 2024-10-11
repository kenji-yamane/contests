def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def cum_freqs(a):
	freqs = []
	curr_freq = [0]*26
	for el in a:
		curr_freq[ord(el) - ord('a')] += 1
		freqs.append(curr_freq.copy())
	return freqs

def diff_maps(x, y):
	diff = []
	for idx in range(len(x)):
		diff.append(x[idx] - y[idx])
	return diff

t = int(input())

for _ in range(t):
	n, q = read_line()

	a = input().strip()
	b = input().strip()

	a_freqs = cum_freqs(a)
	b_freqs = cum_freqs(b)

	for _ in range(q):
		l, r = read_line()
		l -= 1
		r -= 1

		alr = a_freqs[r]
		blr = b_freqs[r]
		if l > 0:
			alr = diff_maps(alr, a_freqs[l - 1])
			blr = diff_maps(blr, b_freqs[l - 1])

		adiffb = diff_maps(alr, blr)
		ans = 0
		for value in adiffb:
			if value > 0:
				ans += value
		print(ans)

