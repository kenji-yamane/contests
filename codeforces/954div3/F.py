def read_line():
	x = input().strip().split(' ')
	return [int(i) for i in x]

tree = []
num_children = []
visited_vertex = []
visited_edge = []
cyclical = []
parents = []
depths = []
branch = []
cycles = []
def choose_two(n):
	return n*(n - 1)//2

def remove_edge(n):
	answer = choose_two(n)
	for vertex in range(n):
		if not cyclical[vertex]:
			children = num_children[vertex]
			answer = min(answer, choose_two(n - children) + choose_two(children))
	return answer

def compute_children(vertex):
	if num_children[vertex] != -1:
		return num_children[vertex]
	answer = 1
	for destination in tree[vertex]:
		answer += compute_children(destination)
	num_children[vertex] = answer
	return answer

def mark_cycles():
	cyclical[0] = True
	cycles.sort(key = lambda x : x[1])
	for cycle in cycles:
		vertex = cycle[0]
		while depths[vertex] != cycle[1] and not cyclical[vertex]:
			cyclical[vertex] = True
			vertex = parents[vertex]

def identify_cycle(graph, descendant, ascendant):
	if branch[descendant] and branch[ascendant]:
		cycles.append([descendant, depths[ascendant]])
	else:
		cycles.append([descendant, 0])
		cycles.append([ascendant, 0])

def dfs(graph, vertex, depth):
	visited_vertex[vertex] = True
	depths[vertex] = depth
	branch[vertex] = True
	for destination in graph[vertex]:
		if destination in visited_edge[vertex]:
			continue
		visited_edge[vertex][destination] = True
		visited_edge[destination][vertex] = True
		if visited_vertex[destination]:
			identify_cycle(graph, vertex, destination)
			continue
		tree[vertex].append(destination)
		parents[destination] = vertex
		dfs(graph, destination, depth + 1)
	branch[vertex] = False

t = int(input())

for _ in range(t):
	n, m = read_line()

	graph = [[] for i in range(n)]
	for _ in range(m):
		u, v = read_line()
		graph[u - 1].append(v - 1)
		graph[v - 1].append(u - 1)

	tree = [[] for i in range(n)]
	num_children = [-1]*n
	visited_vertex = [False]*n
	visited_edge = [{} for i in range(n)]
	cyclical = [False]*n
	parents = [-1]*n
	depths = [-1]*n
	branch = [False]*n
	cycles = []
	dfs(graph, 0, 0)
	mark_cycles()
	compute_children(0)
	print(remove_edge(n))

