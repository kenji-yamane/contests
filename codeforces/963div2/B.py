def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	a_even = []
	max_odd = 0
	for el in a:
		if el%2 == 0:
			a_even.append(el)
		else:
			max_odd = max(max_odd, el)
	if len(a_even) == n or len(a_even) == 0:
		print(0)
		continue

	a_even_greater = []
	a_even_lesser = []
	for el in a_even:
		if el > max_odd:
			a_even_greater.append(el)
		else:
			a_even_lesser.append(el)

	a_even_greater.sort()
	max_odd += sum(a_even_lesser)
	optimal = True
	for el in a_even_greater:
		if max_odd < el:
			optimal = False
			break
		max_odd += el

	if optimal:
		print(len(a_even))
	else:
		print(len(a_even) + 1)

