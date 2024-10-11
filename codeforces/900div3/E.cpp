#include <iostream>
#include <vector>
#include <string>
#include <sstream>

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        int n;
        std::cin >> n;
        std::vector<unsigned int> a(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> a[i];
        }

        int q;
        std::cin >> q;
        std::vector<std::pair<int, int> > queries(q);
        for (int i = 0; i < q; ++i) {
            int l, k;
            std::cin >> l >> k;
            queries[i] = std::make_pair(l, k);
        }

	std::vector<std::vector<std::pair<int, int> > > curves(n, std::vector<std::pair<int, int> >());
	for (int i = a.size() - 2; i >= 0; i--) {
		int plot = (a[i] & a[i + 1]);
		if (plot != a[i]) {
			curves[i].push_back(std::make_pair(i + 1, plot));
		}
		for (int j = 0; j < curves[i + 1].size(); j++) {
			int nextPlot = (plot & curves[i + 1][j].second);
			if (plot != nextPlot) {
				curves[i].push_back(std::make_pair(curves[i + 1][j].first, nextPlot));
			}
			plot = nextPlot;
		}
	}

	std::vector<int> ans(queries.size(), n);
	for (int i = 0; i < queries.size(); i++) {
		int idx = queries[i].first - 1, k = queries[i].second;
		if (a[idx] < k) {
			ans[i] = -1;
			continue;
		}

		ans[i] = n;
		for (int j = 0; j < curves[idx].size(); j++) {
			if (curves[idx][j].second < k) {
				ans[i] = curves[idx][j].first;
				break;
			}
		}
	}
	for (int i = 0; i < ans.size(); i++) {
		std::cout << ans[i] << (i == ans.size() - 1 ? '\n' : ' ');
	}
    }

    return 0;
}

