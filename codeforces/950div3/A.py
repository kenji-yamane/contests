def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

t = int(input())

for _ in range(t):
	n, m = read_line()
	a = input().strip()

	needed = {}
	for idx in range(ord('A'), ord('G') + 1):
		needed[idx] = m

	for problem in a:
		if needed[ord(problem)] > 0:
			needed[ord(problem)] -= 1

	print(sum([needed[key] for key in needed]))

