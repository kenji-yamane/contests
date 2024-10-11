#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <map>
#include <set>

using namespace std;

pair<int, int> cornerToQuery(vector<vector<int> > &grid, int idx) {
	pair<int, int> corner(grid[idx][0], grid[idx][1]);
	if (idx == 0) {
		corner.first--;
		corner.second--;
	} else if (idx == 1) {
		corner.second--;
	} else if (idx == 3) {
		corner.first--;
	}
	return corner;
}

void addQuery(vector<pair<int, int> > &queries, vector<vector<int> > &grid, int idx) {
	pair<int, int> query = cornerToQuery(grid, idx);
	if (query.first >= 0 and query.second >= 0) {
		queries.push_back(query);
	}
}

int chipsInCorner(map<pair<int, int>, int> &answer, vector<vector<int> > &grid, int idx) {
	pair<int, int> query = cornerToQuery(grid, idx);
	if (query.first >= 0 and query.second >= 0) {
		return answer[query];
	} else {
		return 0;
	}
}

int chipsInGrid(map<pair<int, int>, int> &answer, vector<vector<int> > &grid) {
	int ans = chipsInCorner(answer, grid, 2);
	ans -= chipsInCorner(answer, grid, 1);
	ans -= chipsInCorner(answer, grid, 3);
	ans += chipsInCorner(answer, grid, 0);
	return ans;
}

int main() {
	int t;
	cin >> t;

	while (t--) {
		int a, b, n, m;
		cin >> a >> b >> n >> m;
		vector<pair<int, int> > chips;
		while (n--) {
			int x, y;
			cin >> x >> y;
			chips.emplace_back(x - 1, y - 1);
		}
		vector<pair<char, int> > moves;
		while (m--) {
			char c;
			int k;
			cin >> c >> k;
			moves.emplace_back(c, k);
		}

		vector<pair<int, int> > queries;
		vector<vector<int> > grid = {{0, 0}, {a - 1, 0}, {a - 1, b - 1}, {0, b - 1}};
		map<char, pair<int, int> > moveToCorner = {{'U',{0, 3}}, {'D',{1, 2}}, {'L',{0, 1}}, {'R',{2, 3}}};
		map<char, int> moveToSign = {{'U', 1}, {'D', -1}, {'L', 1}, {'R', -1}};
		map<char, int> moveToEdge = {{'U', 0}, {'D', 0}, {'L', 1}, {'R', 1}};
		for (auto &move : moves) {
			pair<int, int> corners = moveToCorner[move.first];
			grid[corners.first][moveToEdge[move.first]] += move.second*moveToSign[move.first];
			grid[corners.second][moveToEdge[move.first]] += move.second*moveToSign[move.first];
			addQuery(queries, grid, corners.first);
			addQuery(queries, grid, corners.second);
		}

		vector<vector<int> > rowColumn, columnRow;
		for (auto &c : chips) {
			vector<int> chip = {c.first, c.second, 0}, invertedChip = {c.second, c.first};
			rowColumn.push_back(chip);
			columnRow.push_back(invertedChip);
		}
		for (auto &c : queries) {
			vector<int> query = {c.first, c.second, 1};
			rowColumn.push_back(query);
		}
		sort(rowColumn.begin(), rowColumn.end());
		sort(columnRow.begin(), columnRow.end());
		map<pair<int, int>, int> columnRowIdx;
		for (int i = 0; i < columnRow.size(); i++) {
			columnRowIdx[make_pair(columnRow[i][1], columnRow[i][0])] = i + 1;
		}
		vector<int> nodesBefore(columnRow.size() + 2, 0);

		map<pair<int, int>, int> answer;
		answer[make_pair(a - 1, b - 1)] = (int)chips.size();
		for (auto &cell : rowColumn) {
			if (cell[2] == 0) {
				int ftIdx = columnRowIdx[make_pair(cell[0], cell[1])];
				while (ftIdx < nodesBefore.size()) {
					nodesBefore[ftIdx] += 1;
					ftIdx += (ftIdx & (-ftIdx));
				}
			} else {
				vector<int> invertedQuery = {cell[1], cell[0]};
				pair<int, int> query(cell[0], cell[1]);
				auto queryColumnRowIt = upper_bound(columnRow.begin(), columnRow.end(), invertedQuery);
				int ftIdx = queryColumnRowIt - columnRow.begin();
				answer[query] = 0;
				while (ftIdx > 0) {
					answer[query] += nodesBefore[ftIdx];
					ftIdx -= (ftIdx & (-ftIdx));
				}
			}
		}

		grid = {{0, 0}, {a - 1, 0}, {a - 1, b - 1}, {0, b - 1}};
		int lastGridChips = chipsInGrid(answer, grid);
		vector<int> scores = {0, 0};
		int currPlayer = 0;
		for (auto &move : moves) {
			pair<int, int> corners = moveToCorner[move.first];
			grid[corners.first][moveToEdge[move.first]] += move.second*moveToSign[move.first];
			grid[corners.second][moveToEdge[move.first]] += move.second*moveToSign[move.first];
			int currentGridChips = chipsInGrid(answer, grid);
			scores[currPlayer] += lastGridChips - currentGridChips;
			currPlayer = (currPlayer + 1)%2;
			lastGridChips = currentGridChips;
		}
		cout << scores[0] << ' ' << scores[1] << endl;
	}

	return 0;
}

