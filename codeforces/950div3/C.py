def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()
	b = read_line()
	m = int(input())
	d = read_line()

	needed_in_d = {}
	for idx in range(len(a)):
		if a[idx] == b[idx]:
			continue
		if b[idx] not in needed_in_d:
			needed_in_d[b[idx]] = 0
		needed_in_d[b[idx]] += 1

	last_needed = -1 
	for idx, el in enumerate(d):
		if el in needed_in_d:
			last_needed = idx
		if el in needed_in_d and needed_in_d[el] > 0:
			needed_in_d[el] -= 1
	needed_present = True
	for key in needed_in_d:
		if needed_in_d[key] != 0:
			needed_present = False
			break
	if not needed_present:
		print('no')
		continue

	if last_needed == m - 1 or d[-1] in b:
		print('yes')
	else:
		print('no')

