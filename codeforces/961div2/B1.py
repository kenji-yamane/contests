# (a + b)x + b1
# a >= 0 => a + b = n => a = n - b => n - b >= 0 => b <= n
# a <= a => n - b <= a => b >= n - a

def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

def max_petals(bouquet):
	ans = 0
	for flower in bouquet:
		ans += flower[0]*flower[1]
	return ans

t = int(input())

for _ in range(t):
	n, m = read_line()
	a = read_line()

	freqs = {}
	for el in a:
		if el not in freqs:
			freqs[el] = 0
		freqs[el] += 1
	freq_arr = list(freqs.items())
	freq_arr.sort()

	bouquets = []
	for idx in range(len(freq_arr)):
		if idx == len(freq_arr) - 1:
			bouquets.append([freq_arr[idx]])
			continue

		if freq_arr[idx + 1][0] == freq_arr[idx][0] + 1:
			bouquets.append([freq_arr[idx], freq_arr[idx + 1]])
		else:
			bouquets.append([freq_arr[idx]])

	ans = 0
	for bouquet in bouquets:
		petals = max_petals(bouquet)
		if petals <= m:
			ans = max(petals, ans)
		elif len(bouquet) == 1:
			while petals > m:
				petals -= bouquet[0][0]
			ans = max(petals, ans)
		else: # n - a <= b <= n
			nflowers = bouquet[0][1] + bouquet[1][1]
			petals = nflowers*bouquet[0][0]
			while nflowers > 0:
				blower = max(0, nflowers - bouquet[0][1])
				bupper = min(bouquet[1][1], nflowers)
				if petals + blower <= m <= petals + bupper:
					ans = m
				elif petals + bupper < m:
					ans = max(petals + bupper, ans)
				petals -= bouquet[0][0]
				nflowers -= 1
	print(ans)

