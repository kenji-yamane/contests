def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def aggregate(a):
	ans = []
	curr = 0
	for el in a:
		curr += el
		ans.append(curr)
	return ans

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()
	s = input().strip()

	agg = aggregate(a)
	left, right = 0, n - 1
	ans = 0
	while left < right:
		if s[left] == 'R':
			left += 1
			continue
		if s[right] == 'L':
			right -= 1
			continue
		ans += agg[right]
		if left > 0:
			ans -= agg[left - 1]
		left += 1
		right -= 1
	print(ans)

