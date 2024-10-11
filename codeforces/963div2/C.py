def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n, k = read_line()
	a = read_line()

	first_cycle = max(a)//k
	lights = [None]*k
	impossible = False
	for el in a:
		if (el//k - first_cycle)%2 == 0:
			turned_on = 1
		else:
			turned_on = -1
		if lights[el%k] != None and lights[el%k] != turned_on:
			impossible = True
			break
		lights[el%k] = turned_on
	if impossible:
		print(-1)
		continue

	total, on, off = 0, 0, 0
	for idx in range(k):
		if lights[idx] == None:
			continue
		if lights[idx] == -1:
			on += 1
		else:
			off += 1
		total += 1

	ans = -1
	for idx in range(k):
		if lights[idx] == None:
			continue
		on += lights[idx]
		off += lights[idx]
		if on == total:
			ans = first_cycle*k + idx
			break
	if ans != -1:
		print(ans)
		continue

	for idx in range(k):
		if lights[idx] == None:
			continue
		on -= lights[idx]
		off -= lights[idx]
		if on == total:
			ans = first_cycle*k + k + idx
			break
	if ans != -1:
		print(ans)
		continue

	print(-1)

