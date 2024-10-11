from heapq import heappush, heappop

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def dijkstra(graph, sources, horseride):
	exploration = []
	distances = [10**12]*len(graph)
	explored = [False]*len(graph)
	for source in sources:
		heappush(exploration, source)
		distances[source[1]] = source[0]
	while len(exploration) > 0:
		node = heappop(exploration)
		explored[node[1]] = True
		for neighbor in graph[node[1]]:
			distance = neighbor[0]//2 if horseride else neighbor[0]
			if distances[node[1]] + distance < distances[neighbor[1]]:
				distances[neighbor[1]] = distances[node[1]] + distance
				heappush(exploration, [distances[neighbor[1]], neighbor[1]])
		while len(exploration) > 0 and explored[exploration[0][1]]:
			_ = heappop(exploration)
	return distances

t = int(input())
for _ in range(t):
	n, m, h = read_line()
	graph = [[] for _ in range(n)]
	a = read_line()
	for _ in range(m):
		u, v, w = read_line()
		graph[u - 1].append([w, v - 1])
		graph[v - 1].append([w, u - 1])
	marian_foot = dijkstra(graph, [[0, 0]], False)
	marian_horses = dijkstra(graph, [[marian_foot[el - 1], el - 1] for el in a], True)
	marian = marian_foot.copy()
	for idx in range(n):
		marian[idx] = min(marian[idx], marian_horses[idx])
	robin_foot = dijkstra(graph, [[0, n - 1]], False)
	robin_horses = dijkstra(graph, [[robin_foot[el - 1], el - 1] for el in a], True)
	robin = robin_foot.copy()
	for idx in range(n):
		robin[idx] = min(robin[idx], robin_horses[idx])

	ans = max(robin[0], marian[0])
	for idx in range(n):
		ans = min(ans, max(robin[idx], marian[idx]))
	if ans == 10**12:
		print(-1)
	else:
		print(ans)

