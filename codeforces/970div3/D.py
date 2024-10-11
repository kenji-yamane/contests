def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	p_1 = read_line()
	p = [el - 1 for el in p_1]
	s = input().strip()

	visited = [False]*len(p)
	ans = [-1]*len(p)
	for idx in range(len(p)):
		if visited[idx]:
			continue

		curr = p[idx]
		cycle = [curr]
		blacks = 0
		if s[curr] == '0':
			blacks += 1
		while p[curr] != p[idx]:
			curr = p[curr]
			cycle.append(curr)
			if s[curr] == '0':
				blacks += 1
		for el in cycle:
			visited[el] = True
			ans[el] = blacks

	print(*ans)

