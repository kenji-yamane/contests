def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	s = input().strip()

	freqs = [0]*26
	for el in s:
		freqs[ord(el) - ord('a')] += 1

	idx = 0
	ans = []
	while n > 0:
		if freqs[idx] > 0:
			ans.append(chr(idx + ord('a')))
			freqs[idx] -= 1
			n -= 1
		idx += 1
		idx %= 26
	print(''.join(ans))

