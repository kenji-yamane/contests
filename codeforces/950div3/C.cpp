#include<map>
#include<vector>
#include<iostream>

using namespace std;

int main() {
	int t;
	cin >> t;

	while (t--) {
		int n;
		cin >> n;
		vector<int> a;
		while (n--) {
			int x;
			cin >> x;
			a.push_back(x);
		}
		n = a.size();
		vector<int> b;
		map<int, int> bMap;
		while (n--) {
			int x;
			cin >> x;
			b.push_back(x);
			bMap[x] = 0;
		}
		int m;
		cin >> m;
		vector<int> d;
		while (m--) {
			int x;
			cin >> x;
			d.push_back(x);
		}
		map<int, int> needed;
		for (int i = 0; i < a.size(); i++) {
			if (a[i] == b[i]) continue;
			if (needed.find(b[i]) == needed.end()) needed[b[i]] = 0;
			needed[b[i]]++;
		}

		int last_needed = -1;
		for (int i = 0; i < d.size(); i++) {
			if (needed.find(d[i]) == needed.end()) continue;
			last_needed = i;
			if (needed[d[i]] > 0) needed[d[i]]--;
		}

		bool needed_present = true;
		for (map<int, int>::iterator it = needed.begin(); it != needed.end(); it++) {
			if (it->second != 0) needed_present = false;
		}
		if (!needed_present) {
			cout << "no" << endl;
			continue;
		}

		if (last_needed == d.size() - 1 || bMap.find(d.back()) != bMap.end()) {
			cout << "yes" << endl;
		} else {
			cout << "no" << endl;
		}
	}

	return 0;
}
