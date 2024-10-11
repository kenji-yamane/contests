#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef pair<int, int> pii;

int remainder(int n, int k) {
	if (n%k == 0) return k;
	return n%k;
}

int blocks(int n, int k) {
	if (n%k == 0) return n/k;
	return n/k + 1;
}

int longestChain(vector<int> &a, int x, int n, int k) {
	vector<int> memo(a.size(), 0);
	for (int i = 0; i < remainder(n, k); i++) if (a[i] >= x) memo[i] = 1;
	for (int j = 0; j*k < n; j++) if (a[j*k] >= x) memo[j*k] = 1;
	for (int i = 0; i < remainder(n, k); i++) {
		for (int j = 0; j*k + i < n; j++) {
			if ((j + 1)*k + i < n) memo[(j + 1)*k + i] = max(memo[(j + 1)*k + i], memo[j*k + i]);
			if (j*k + i + 1 < n) {
				int longestSoFar = memo[j*k + i];
				if (a[j*k + i + 1] >= x) longestSoFar++;
				memo[j*k + i + 1] = max(memo[j*k + i + 1], longestSoFar);
			}
		}
	}
	return memo.back();
}

vector<int> deduplicate(vector<int> arr) {
	vector<int> ans;
	int last = -1;
	for (auto &c : arr) {
		if (c == last) continue;
		ans.push_back(c);
		last = c;
	}
	return ans;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	cin >> t;

	while (t--) {
		int n, k;
		cin >> n >> k;
		vector<int> a;
		while (n--) {
			int ai;
			cin >> ai;
			a.push_back(ai);
		}
		n = a.size();

		vector<int> candidates;
		for (int i = 0; i < remainder(n, k); i++)
			for (int j = 0; j*k + i < n; j++)
				candidates.push_back(a[j*k + i]);
		sort(candidates.begin(), candidates.end());
		candidates = deduplicate(candidates);

		if (longestChain(a, candidates.back(), n, k) > remainder(n, k)/2) {
			cout << candidates.back() << endl;
			continue;
		}
		int ini = 0, fin = candidates.size() - 1;
		while (fin != ini + 1) {
			int middle = (ini + fin)/2;
			if (longestChain(a, candidates[middle], n, k) > remainder(n, k)/2) {
				ini = middle;
			} else {
				fin = middle;
			}
		}
		cout << candidates[ini] << endl;
	}

	return 0;
}

