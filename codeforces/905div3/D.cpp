#include <iostream>
#include <map>

using namespace std;

int main() {
	int q;
	cin >> q;

	map<int, int> inis, fins;
	while (q--) {
		char op;
		int l, r;
		cin >> op >> l >> r;
		if (op == '+') {
			if (inis.find(l) == inis.end()) {
				inis[l] = 0;
			}
			inis[l]++;
			if (fins.find(r) == fins.end()) {
				fins[r] = 0;
			}
			fins[r]++;
		} else {
			inis[l]--;
			if (inis[l] == 0) {
				inis.erase(l);
			}
			fins[r]--;
			if (fins[r] == 0) {
				fins.erase(r);
			}
		}
		if (inis.empty() || inis.rbegin()->first <= fins.begin()->first) {
			cout << "NO" << endl;
		} else {
			cout << "YES" << endl;
		}
	}

	return 0;
}
