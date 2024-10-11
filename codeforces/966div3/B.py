def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	seats = [0]*n
	seats[a[0] - 1] = 1
	followed = True
	for a_idx in range(1, len(a)):
		idx = a[a_idx] - 1
		seats[idx] = 1
		occupied_neighbors = 0
		if idx > 0 and seats[idx - 1] == 1:
			occupied_neighbors += 1
		if idx < n - 1 and seats[idx + 1] == 1:
			occupied_neighbors += 1
		if occupied_neighbors == 0:
			followed = False
	if followed:
		print('yes')
	else:
		print('no')

