def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n, k = read_line()

	people = read_line()
	benefited = 0
	money = 0
	for person in people:
		if person == 0 and money > 0:
			money -= 1
			benefited += 1
		if person >= k:
			money += person
	print(benefited)

