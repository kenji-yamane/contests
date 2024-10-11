# n even: true false false true false false true
# n odd: false false true true false false true

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())
for _ in range(t):
	n, d, k = read_line()
	starts = [0]*n
	ends = [0]*n
	for _ in range(k):
		l, r = read_line()
		starts[l - 1] += 1
		ends[r - 1] += 1

	curr = 0
	for idx in range(d - 1):
		curr += starts[idx]
	intersections = []
	jobs = []
	for idx in range(d - 1, n):
		curr += starts[idx]
		intersections.append(curr)
		curr -= ends[idx - d + 1]

	m, M = min(intersections), max(intersections)
	ans = []
	for idx in range(n):
		if intersections[idx] == M:
			ans.append(idx + 1)
			break
	for idx in range(n):
		if intersections[idx] == m:
			ans.append(idx + 1)
			break
	print(*ans)

