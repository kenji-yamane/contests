#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int mean(vector<int> &a) {
	int amin = 1e9 + 1, amax = -1;
	for (auto &el : a) {
		if (el < amin) amin = el;
		if (el > amax) amax = el;
	}
	return (amin + amax)/2;
}

void operate(vector<int> &a, int mean) {
	for (auto &el : a) el = abs(el - mean);
}

bool zeros(vector<int> &a) {
	for (auto &el : a) if (el != 0) return false;
	return true;
}

bool equable(vector<int> &a) {
	for (auto &el : a) {
		if (el%2 != a[0]%2) return false;
	}
	return true;
}

int main() {
	int t;
	cin >> t;

	while (t--) {
		int n;
		cin >> n;

		vector<int> a;
		while (n--) {
			int ai;
			cin >> ai;
			a.push_back(ai);
		}

		if (!equable(a)) {
			cout << -1 << endl;
			continue;
		}

		vector<int> operations;
		while (!zeros(a)) {
			operations.push_back(mean(a));
			operate(a, mean(a));
			if (operations.size() == 40) break;
		}

		if (!zeros(a)) {
			cout << -1 << endl;
			continue;
		}

		cout << operations.size() << endl;
		for (int i = 0; i < operations.size(); i++)
			cout << operations[i] << (i == operations.size() - 1 ? '\n' : ' ');
		if (operations.empty()) cout << endl;
	}

	return 0;
}

