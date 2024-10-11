def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

t = int(input())

for _ in range(t):
	n, c, k = read_line()
	text = input().strip()

	last_seen = [-1]*c
	set_routes = [0]*n
	for idx in range(n - 1, -1, -1):
		last_seen[ord(text[idx]) - ord('A')] = idx
		for case in range(c):
			if last_seen[case] != -1 and last_seen[case] - idx <= k:
				set_routes[idx] |= (1 << case)

	set_covers = [0]*2**(c + 1)
	for set in set_routes:
		set_covers[set] += 1

