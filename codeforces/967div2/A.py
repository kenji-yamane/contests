def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	counts = {}
	for el in a:
		if el not in counts:
			counts[el] = 0
		counts[el] += 1

	max_count = 0
	for count in counts.values():
		max_count = max(max_count, count)
	print(len(a) - max_count)

