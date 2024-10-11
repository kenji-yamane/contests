def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	frequencies = {}
	for el in a:
		if el not in frequencies:
			frequencies[el] = 0
		frequencies[el] += 1

	winning = False
	for frequency in frequencies.values():
		if frequency%2 == 1:
			winning = True
	if winning:
		print('yes')
	else:
		print('no')

