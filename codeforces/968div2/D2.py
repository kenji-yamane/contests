# 1 3
# 0 1
# 2 3
# 3 + 3 + 3 + 3 + 4
# 16

# 1 3
# 0 2
# 2 4
# 20

# 0 3

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def deduplicate(edges):
	sorted_edges = edges.copy()
	sorted_edges.sort(key = lambda x : [-x[1], x[0]])
	ans, last = [], None
	for edge in sorted_edges:
		if edge == last:
			continue
		ans.append(edge.copy())
		last = edge.copy()
	return ans

def mexes(sequence):
	visited = [False]*(len(sequence) + 2)
	for el in sequence:
		if el < len(sequence) + 2:
			visited[el] = True
	ans = []
	for idx in range(len(visited)):
		if not visited[idx]:
			ans.append(idx)
		if len(ans) == 2:
			break
	return ans

def outsider_strategy(edges, optimal):
	ans = max([edge[0] for edge in edges])
	freqs = [0]*(ans + 1)
	for edge in edges:
		freqs[edge[0]] += 1
	for edge in edges:
		if freqs[edge[0]] > 1:
			ans = max(ans, optimal[edge[0]])
	return ans

def dfs(vertex, graph, optimal, current):
	if optimal[vertex] != -1:
		return
	optimal[vertex] = current
	for neighbor in graph[vertex]:
		dfs(neighbor, graph, optimal, current)

t = int(input())

for _ in range(t):
	n, m = read_line()
	l = []
	sequences = []
	for _ in range(n):
		sequence = read_line()
		l.append(sequence[0])
		sequences.append(sequence[1:])

	n_vertexes = max(l) + 2
	graph = [[] for i in range(n_vertexes)]
	edges = deduplicate([mexes(sequence) for sequence in sequences])
	for edge in edges:
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])

	optimal = [-1]*n_vertexes
	for edge in edges:
		dfs(edge[1], graph, optimal, edge[1])
	outsider_optimal = outsider_strategy([mexes(sequence) for sequence in sequences], optimal)

	ans = 0
	for k in range(n_vertexes):
		if k > m:
			break
		if optimal[k] == -1:
			ans += max(outsider_optimal, k)
		else:
			ans += max(outsider_optimal, optimal[k])
	if m >= n_vertexes:
		ans += (n_vertexes + m)*(m - n_vertexes + 1)//2
	print(ans)

