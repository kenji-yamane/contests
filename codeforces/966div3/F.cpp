#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

typedef pair<int, int> pii;

int fill(vector<vector<int> > &memo, vector<pii> &rectangles, int i, int k) {
	if (k <= 0) return 0;
	if (i >= rectangles.size()) return 100000000;
	if (memo[i][k] != -1) return memo[i][k];
	int ans = 100000000;
	int a = rectangles[i].first, b = rectangles[i].second;
	int ops = 0;
	for (int points = 0; points <= rectangles[i].first + rectangles[i].second; points++) {
		if (points == rectangles[i].first + rectangles[i].second - 1) continue;
		ans = min(ans, ops + fill(memo, rectangles, i + 1, k - points));
		int smallest = min(a, b), biggest = max(a, b);
		ops += smallest;
		biggest -= 1;
		a = smallest;
		b = biggest;
	}
	return memo[i][k] = ans;
}

int main() {
	int t;
	cin >> t;

	while (t--) {
		int n, k;
		cin >> n >> k;

		vector<pii> rectangles;
		while (n--) {
			int a, b;
			cin >> a >> b;
			rectangles.emplace_back(a, b);
		}

		vector<vector<int> > memo(rectangles.size(), vector<int>(k + 1, -1));
		int ans = fill(memo, rectangles, 0, k);
		if (ans == 100000000) cout << -1 << endl;
		else cout << ans << endl;
	}

	return 0;
}

