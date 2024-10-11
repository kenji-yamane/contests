#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>

using namespace std;

long long chooseTwo(int n) {
	return (long long)n*(n - 1)/2;
}

vector<vector<int> > tree;
vector<int> numChildren;
vector<bool> visitedVertex;
vector<map<int, bool> > visitedEdge;
vector<bool> cyclical;
vector<int> parents;
vector<int> depths;
vector<bool> branch;
vector<pair<int, int> > cycles;
long long removeEdge(int n) {
	long long answer = chooseTwo(n);
	for (int vertex = 0; vertex < n; vertex++) {
		if (!cyclical[vertex]) {
			int children = numChildren[vertex];
			answer = min(answer, chooseTwo(n - children) + chooseTwo(children));
		}
	}
	return answer;
}

int computeChildren(int vertex) {
	if (numChildren[vertex] != -1) {
		return numChildren[vertex];
	}
	int answer = 1;
	for (auto &destination : tree[vertex]) {
		answer += computeChildren(destination);
	}
	return numChildren[vertex] = answer;
}

bool compareCycles(const pair<int, int> &a, const pair<int, int> &b) {
	return (a.second < b.second);
}
void markCycles() {
	cyclical[0] = true;
	sort(cycles.begin(), cycles.end(), compareCycles);
	for (auto &cycle : cycles) {
		int vertex = cycle.first;
		while (depths[vertex] != cycle.second && !cyclical[vertex]) {
			cyclical[vertex] = true;
			vertex = parents[vertex];
		}
	}
}

void identifyCycle(int descendant, int ascendant) {
	if (branch[descendant] && branch[ascendant]) {
		cycles.emplace_back(descendant, depths[ascendant]);
	} else {
		cycles.emplace_back(descendant, 0);
		cycles.emplace_back(ascendant, 0);
	}
}

void dfs(const vector<vector<int> > &graph, int vertex, int depth) {
	visitedVertex[vertex] = true;
	depths[vertex] = depth;
	branch[vertex] = true;
	for (auto &destination : graph[vertex]) {
		if (visitedEdge[vertex].find(destination) != visitedEdge[vertex].end()) {
			continue;
		}
		visitedEdge[vertex][destination] = true;
		visitedEdge[destination][vertex] = true;
		if (visitedVertex[destination]) {
			identifyCycle(vertex, destination);
			continue;
		}
		tree[vertex].push_back(destination);
		parents[destination] = vertex;
		dfs(graph, destination, depth + 1);
	}
	branch[vertex] = false;
}

int main() {
	int t;
	cin >> t;

	while (t--) {
		int n, m;
		cin >> n >> m;

		vector<vector<int> > graph(n, vector<int>());
		while (m--) {
			int u, v;
			cin >> u >> v;
			graph[u - 1].push_back(v - 1);
			graph[v - 1].push_back(u - 1);
		}

		tree = vector<vector<int> >(n, vector<int>());
		numChildren = vector<int>(n, -1);
		visitedVertex = vector<bool>(n, false);
		visitedEdge = vector<map<int, bool> >(n, map<int, bool>());
		cyclical = vector<bool>(n, false);
		parents = vector<int>(n, -1);
		depths = vector<int>(n, -1);
		branch = vector<bool>(n, false);
		cycles.clear();
		dfs(graph, 0, 0);
		markCycles();
		computeChildren(0);
		cout << removeEdge(n) << endl;
	}

	return 0;
}

