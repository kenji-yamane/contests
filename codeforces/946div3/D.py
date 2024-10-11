def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def greedy_on_zero(s):
	symmetrics = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}
	p = ['R']
	found = False
	for i in range(1, len(s)):
		if s[i] == symmetrics[s[0]] and not found:
			p.append('R')
			found = True
		else:
			p.append('H')
	return ''.join(p)

t = int(input())

for _ in range(t):
	n = int(input())
	s = list(input().strip())

	vertical, horizontal = 0, 0
	for direction in s:
		if direction == 'N':
			vertical += 1
		elif direction == 'S':
			vertical -= 1
		elif direction == 'E':
			horizontal += 1
		elif direction == 'W':
			horizontal -= 1

	if vertical == 0 and horizontal == 0 and len(s) == 2:
		print('NO')
		continue

	if vertical == 0 and horizontal == 0:
		print(greedy_on_zero(s))
		continue

	if vertical%2 == 1 or horizontal%2 == 1:
		print('NO')
		continue

	aim_y = None
	if vertical > 0:
		aim_y = 'N'
	elif vertical < 0:
		aim_y = 'S'
	vertical = abs(vertical)

	aim_x = None
	if horizontal > 0:
		aim_x = 'E'
	elif horizontal < 0:
		aim_x = 'W'
	horizontal = abs(horizontal)

	bots = ['R', 'H']
	vertical_bot = 0
	horizontal_bot = 0
	p = []
	for el in s:
		if el == aim_y and vertical > 0:
			p.append(bots[vertical_bot])
			vertical_bot = (vertical_bot + 1)%2
			vertical -= 1
		elif el == aim_x and horizontal > 0:
			p.append(bots[horizontal_bot])
			horizontal_bot = (horizontal_bot + 1)%2
			horizontal -= 1
		else:
			p.append('R')
	print(''.join(p))

