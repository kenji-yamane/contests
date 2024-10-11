#include <iostream>
#include <vector>
#include <map>

using namespace std;

int vmin(vector<int> a) {
	int ans = a[0];
	for (auto &el : a) {
		ans = min(ans, el);
	}
	return ans;
}

int vmax(vector<int> a) {
	int ans = a[0];
	for (auto &el : a) {
		ans = max(ans, el);
	}
	return ans;
}

int main() {
	int t;
	cin >> t;
	while (t--) {
		int n, d, k;
		cin >> n >> d >> k;
		vector<int> starts(n, 0);
		vector<int> ends(n, 0);
		while (k--) {
			int l, r;
			cin >> l >> r;
			starts[l - 1]++;
			ends[r - 1]++;
		}

		int curr = 0;
		vector<int> jobs;
		for (int i = 0; i < n; i++) {
			curr += starts[i];
			jobs.push_back(curr);
			cout << curr << " ";
			curr -= ends[i];
		}
		cout << endl;

		map<int, int> visit;
		for (int i = 0; i < d - 1; i++) {
			if (visit.find(jobs[i]) == visit.end()) visit[jobs[i]] = 0;
			visit[jobs[i]]++;
		}
		vector<int> intersections;
		for (int i = d - 1; i < n; i++) {
			if (visit.find(jobs[i]) == visit.end()) visit[jobs[i]] = 0;
			visit[jobs[i]]++;
			intersections.push_back(visit.rbegin()->first);
			visit[jobs[i - d + 1]]--;
			if (visit[jobs[i - d + 1]] == 0) visit.erase(jobs[i - d + 1]);
		}
		int brother = -1, mother = -1;
		int m = vmin(intersections), M = vmax(intersections);
		for (int i = 0; i < intersections.size(); i++) {
			if (intersections[i] == m && mother == -1) mother = i;
			if (intersections[i] == M && brother == -1) brother = i;
		}
		cout << brother + 1 << " " << mother + 1 << endl;
	}

	return 0;
}
