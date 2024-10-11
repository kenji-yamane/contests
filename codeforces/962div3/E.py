# 100110

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	s = input().strip()

	agg_diff = [0]
	for el in s:
		if el == '0':
			agg_diff.append(agg_diff[-1] - 1)
		else:
			agg_diff.append(agg_diff[-1] + 1)

	agg_right = [0]*len(agg_diff)
	right_per_value = {}
	for idx in range(len(agg_diff) - 1, -1, -1):
		if agg_diff[idx] not in right_per_value:
			right_per_value[agg_diff[idx]] = 0
		agg_right[idx] = right_per_value[agg_diff[idx]]
		right_per_value[agg_diff[idx]] += len(agg_diff) - idx

	ans = 0
	for idx in range(0, len(agg_right)):
		ans += agg_right[idx]*(idx + 1)
		ans %= 10**9 + 7
	print(ans)

