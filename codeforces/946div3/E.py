def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	m, x = read_line()

	opportunities = []
	for _ in range(m):
		c, h = read_line()
		opportunities.append([c, h])

	full_happy = sum([el[1] for el in opportunities])
	max_cost = 50*10**8
	impossible_cost = max_cost + 1
	happiness = [[impossible_cost]*(full_happy + 1) for _ in range(m)]
	happiness[0][0] = 0
	if opportunities[0][0] == 0:
		happiness[0][opportunities[0][1]] = 0

	for month in range(1, m):
		for h in range(full_happy + 1):
			if happiness[month - 1][h] == impossible_cost:
				continue

			current_cost = happiness[month - 1][h]
			happiness[month][h] = min(happiness[month][h], current_cost)
			current_cost += opportunities[month][0]
			new_happiness = h + opportunities[month][1]
			if current_cost <= x*month:
				happiness[month][new_happiness] = min(current_cost, happiness[month][new_happiness])

	answer = 0
	for h in range(full_happy + 1):
		if happiness[-1][h] < impossible_cost:
			answer = h
	print(answer)

