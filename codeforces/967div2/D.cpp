#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>

using namespace std;

int next(map<int, int> &options, bool maximize) {
	if (maximize) {
		return options.rbegin()->first;
	} else {
		return options.begin()->first;
	}
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
		n = a.size();

		unordered_map<int, int> remaining;
		for (auto &el : a) {
			if (remaining.find(el) == remaining.end()) {
				remaining[el] = 0;
			}
			remaining[el]++;
		}

		map<int, int> options;
		vector<int> answer;
		unordered_map<int, bool> answered;
		int cursor = 0;
		bool maximize = true;
		for (auto &el : a) {
			remaining[el]--;
			if (answered.find(el) != answered.end()) continue;
			if (options.find(el) == options.end()) options[el] = 0;
			options[el]++;
			if (remaining[el] > 0) continue;

			bool answeredEl = false;
			while (not answeredEl) {
				if (next(options, maximize) == el) answeredEl = true;
				for (; a[cursor] != next(options, maximize); cursor++) {
					if (answered.find(a[cursor]) != answered.end()) continue;
					options[a[cursor]]--;
					if (options[a[cursor]] == 0) options.erase(a[cursor]);
				}
				answer.push_back(next(options, maximize));
				answered[next(options, maximize)] = true;
				options.erase(next(options, maximize));
				maximize = not maximize;
				cursor++;
			}
		}

		cout << answer.size() << endl;
		for (int i = 0; i < answer.size() - 1; i++) cout << answer[i] << " ";
		cout << answer.back() << endl;
	}

	return 0;
}

