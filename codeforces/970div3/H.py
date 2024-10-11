def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def deduplicate(arr):
	arr.sort()
	ans = []
	last = None
	for el in arr:
		if last != el:
			ans.append(el)
		last = el
	return ans

def aggregate(arr):
	ans = [0]*(len(arr) + 1)
	for el in arr:
		ans[el] += 1
	for idx in range(1, len(ans)):
		ans[idx] += ans[idx - 1]
	return ans

def sorted_idx(agg, x, idx):
	ans = agg[idx]
	idx += x
	while idx - idx%x < len(agg):
		ans += agg[min(idx, len(agg) - 1)] - agg[idx - idx%x - 1]
		idx += x
	return ans

def median(n, agg, x):
	median_idx = n//2
	ini, fin = 0, x - 1
	if sorted_idx(agg, x, ini) > median_idx:
		return ini

	while ini + 1 != fin:
		middle = (ini + fin)//2
		if sorted_idx(agg, x, middle) > median_idx:
			fin = middle
		else:
			ini = middle
	return fin

t = int(input())

for _ in range(t):
	n, q = read_line()
	a = read_line()
	agg = aggregate(a)

	original_queries = []
	for _ in range(q):
		original_queries.append(int(input()))
	queries = original_queries.copy()
	queries = deduplicate(queries)

	ans = [0]*(n + 1)
	for x in queries:
		if n == 1:
			ans[x] = a[0]%x
		else:
			ans[x] = median(n, agg, x)

	print(*[ans[x] for x in original_queries])

