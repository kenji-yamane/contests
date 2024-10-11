# (a + b)x + b1
# a >= 0 => a + b = n => a = n - b => n - b >= 0 => b <= n
# a <= a => n - b <= a => b >= n - a
# bouquet[0][0]*quotient <= petals - m
# petals - bouquet[0][0]*quotient >= m
# bouquet[0][0]*(quotient + 1) > petals - m
# petals - bouquet[0][0]*(quotient + 1) < m

def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

def ceil(x, y):
	if x <= 0:
		return 0
	elif x%y == 0:
		return x//y
	else:
		return x//y + 1

def max_petals(bouquet):
	ans = 0
	for flower in bouquet:
		ans += flower[0]*flower[1]
	return ans

def max_in_interval(bouquet, nflowers, m):
	petals = nflowers*bouquet[0][0]
	blower = max(0, nflowers - bouquet[0][1])
	bupper = min(bouquet[1][1], nflowers)
	if petals + blower <= m <= petals + bupper:
		return m
	elif petals + bupper < m:
		return petals + bupper
	else:
		return 0

t = int(input())

for _ in range(t):
	n, m = read_line()
	a = read_line()
	c = read_line()

	freq_arr = []
	for i in range(n):
		freq_arr.append([a[i], c[i]])
	freq_arr.sort()

	bouquets = []
	for idx in range(len(freq_arr)):
		bouquet = [freq_arr[idx]]
		if idx < len(freq_arr) - 1 and freq_arr[idx + 1][0] == freq_arr[idx][0] + 1:
			bouquet.append(freq_arr[idx + 1])
		bouquets.append(bouquet)

	ans = 0
	for bouquet in bouquets:
		petals = max_petals(bouquet)
		if petals <= m:
			ans = max(petals, ans)
		elif len(bouquet) == 1:
			optimal_count = ceil(petals - m, bouquet[0][0])
			petals -= bouquet[0][0]*optimal_count
			ans = max(petals, ans)
		else: # n - a <= b <= n
			petals = (bouquet[0][1] + bouquet[1][1])*bouquet[0][0]
			optimal_count = ceil(petals - m, bouquet[0][0])
			nflowers = bouquet[0][1] + bouquet[1][1] - optimal_count
			ans = max(ans, max_in_interval(bouquet, nflowers, m))

			overshoot = (bouquet[0][1] + bouquet[1][1])*(bouquet[0][0] + 1)
			optimal_count = ceil(overshoot - bouquet[0][1] - m, bouquet[1][0])
			nflowers = bouquet[0][1] + bouquet[1][1] - min(optimal_count, bouquet[1][1])
			ans = max(ans, max_in_interval(bouquet, nflowers, m))
	print(ans)

