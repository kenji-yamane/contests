#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <bitset>

using namespace std;

vector<int> bottomUp;
int getCoverageFromChildren(vector<int> &partialCovers, int set, int c) {
	if (bottomUp[set] != -1) return bottomUp[set];

	int ans = partialCovers[set];
	for (int cs = 0; cs < c; cs++) {
		int child = set;
		child &= ~(1 << cs);
		if (set == child) continue;
		ans += getCoverageFromChildren(partialCovers, child, c);
	}
	return bottomUp[set] = ans;
}

vector<int> topDown;
int getCoverageFromParents(vector<int> &partialCovers, int set, int c) {
	if (topDown[set] != -1) return topDown[set];

	int ans = partialCovers[set];
	for (int cs = 0; cs < c; cs++) {
		int child = set;
		child |= (1 << cs);
		if (set == child) continue;
		ans += getCoverageFromParents(partialCovers, child, c);
	}
	return topDown[set] = ans;
}

int setSize(int set) {
	int ans = 0;
	while (set > 0) {
		ans += (set & 1);
		set >>= 1;
	}
	return ans;
}

void printArr(vector<int> arr) {
	for (auto &el : arr) cout << el << ' ';
	cout << endl;
}

int main() {
	int t;
	cin >> t;

	while (t--) {
		int n, c, k;
		cin >> n >> c >> k;

		string text;
		cin >> text;
		vector<int> lastSeen(c, -1);
		vector<int> setRoutes(n + 1, 0);
		for (int i = n - 1; i >= 0; i--) {
			lastSeen[text[i] - 'A'] = i;
			for (int cs = 0; cs < c; cs++)
				if (lastSeen[cs] != -1 and lastSeen[cs] - i <= k)
					setRoutes[i + 1] |= (1 << cs);
		}
		for (int cs = 0; cs < c; cs++)
			if (lastSeen[cs] != -1 and lastSeen[cs] + 1 <= k)
				setRoutes[0] |= (1 << cs);
		printArr(setRoutes);

		vector<int> partialCovers(1 << c, 0);
		for (auto &set : setRoutes) partialCovers[set]++;

		bottomUp = vector<int>(1 << c, -1);
		bottomUp[0] = 0;
		getCoverageFromChildren(partialCovers, (1 << c) - 1, c);

		topDown = vector<int>(1 << c, -1);
		topDown[(1 << c) - 1] = partialCovers[(1 << c) - 1];
		getCoverageFromParents(partialCovers, 0, c);

		printArr(bottomUp);
		printArr(topDown);
		printArr(partialCovers);
		int ans = c;
		for (int set = 1; set < bottomUp.size(); set++)
			if (bottomUp[set] + topDown[set] - partialCovers[set] == n + 1)
				ans = min(ans, setSize(set));
		cout << ans << endl;
	}

	return 0;
}

