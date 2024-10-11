def read_line():
	x = input().strip().split(' ')
	return [int(i) for i in x]

def deduplicate(arr):
	deduplicated = []
	for i in arr:
		if len(deduplicated) == 0 or deduplicated[-1] != i:
			deduplicated.append(i)
	return deduplicated

t = int(input())

for _ in range(t):
	n, m = read_line()
	s = list(input().strip())
	m = read_line()
	m.sort()
	m = deduplicate(m)
	c = sorted(input().strip())
	for i in range(len(m)):
		s[m[i] - 1] = c[i]
	print(''.join(s))

