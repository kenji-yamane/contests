def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	s = input().strip()

	freqs = [0]*5
	for el in s:
		if el == '?':
			freqs[4] += 1
		else:
			freqs[ord(el) - ord('A')] += 1

	ans = 0
	for idx in range(4):
		ans += min(freqs[idx], n)
	print(ans)

