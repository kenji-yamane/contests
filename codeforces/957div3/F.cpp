#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void printVec(vector<int> arr) {
	for (auto &el : arr) cout << el << ' ';
	cout << endl;
}

vector<int> sieve(int n) {
	vector<bool> isPrime(n + 1, true);
	isPrime[0] = isPrime[1] = false;
	for (int i = 2; i < n + 1; i++) {
		if (not isPrime[i]) continue;

		for (int j = 2; i*j < n + 1; j++) isPrime[i*j] = false;
	}

	vector<int> primes;
	for (int i = 0; i < n + 1; i++) {
		if (isPrime[i]) primes.push_back(i);
	}
	return primes;
}

vector<int> factorize(vector<int> &primes, int x) {
	vector<int> factors;
	for (auto &prime : primes) {
		if (prime > x) break;
		if (x%prime == 0) factors.push_back(prime);
	}
	return factors;
}

vector<int> powerize(vector<int> &factors, int x) {
	vector<int> powers;
	for (auto &factor : factors) {
		powers.push_back(0);
		int copyX = x;
		while (copyX%factor == 0) copyX /= factor, powers.back()++;
	}
	return powers;
}

void generateStates(vector<vector<int> > &states, vector<int> &powers, vector<int> state, int idx) {
	if (idx == powers.size()) {states.push_back(state); return;}
	state.push_back(0);
	for (int i = 0; i <= powers[idx]; i++) {
		generateStates(states, powers, state, idx + 1);
		state.back()++;
	}
}

int main() {
	int t;
	cin >> t;
	vector<int> primes = sieve(100000);

	while (t--) {
		int n, x;
		cin >> n >> x;
		vector<int> primes = sieve(x);
		vector<int> xfactors = factorize(primes, x);
		vector<int> xpowers = powerize(xfactors, x);

		vector<vector<int> > states;
		vector<int> state;
		generateStates(states, xpowers, state, 0);
		sort(states.begin(), states.end());

		vector<int> a;
		while (n--) {
			int ai;
			cin >> ai;
			a.push_back(ai);
		}

		vector<int> xdivs;
		for (auto &el : a) if (x%el == 0) xdivs.push_back(el);
		vector<vector<int> > xdivspowers;
		for (auto &el : xdivs) xdivspowers.push_back(powerize(xfactors, el));

		vector<vector<bool> > multiplications(xdivs.size() + 1, vector<bool>(states.size(), false));
		int ans = 1;
		multiplications[0][0] = true;
		for (int i = 0; i < xdivspowers.size(); i++) {
			bool foundX = false;
			for (int j = 0; j < states.size(); j++) {
				if (multiplications[i][j] == false) continue;
				multiplications[i + 1][j] = true;

				vector<int> multiply = states[j];
				bool tooBig = false;
				for (int k = 0; k < multiply.size(); k++) {
					multiply[k] += xdivspowers[i][k];
					if (multiply[k] > xpowers[k]) tooBig = true;
				}
				if (tooBig) continue;
				int multiplyIdx = lower_bound(states.begin(), states.end(), multiply) - states.begin();
				if (multiplyIdx == states.size() - 1) {foundX = true; break;}
				multiplications[i + 1][multiplyIdx] = true;
			}
			if (foundX) {
				ans += 1;
				for (int j = 0; j < states.size(); j++){
					multiplications[i][j] = false;
					multiplications[i + 1][j] = false;
				}
				multiplications[i][0] = true;
				i--;
			}
		}
		cout << ans << endl;
	}

	return 0;
}
