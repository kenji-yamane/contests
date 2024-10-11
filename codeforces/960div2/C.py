def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

def madify(arr):
	freqs = {}
	max_rep = 0
	ans = []
	for el in arr:
		if el not in freqs:
			freqs[el] = 0
		freqs[el] += 1
		if freqs[el] > 1 and el > max_rep:
			max_rep = el
		ans.append(max_rep)
	return ans

def get_reps(arr):
	reps = {}
	for idx, el in enumerate(arr):
		if el == 0:
			continue
		if el not in reps:
			reps[el] = [idx, idx]
		reps[el][1] = idx
	return reps

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	ans = 0
	ans += sum(a)
	a = madify(a)
	ans += sum(a)
	a = madify(a)

	reps = get_reps(a)
	for el, interval in reps.items():
		ans += el*(interval[1] - interval[0] + 1)*(len(a) - 1 - interval[1])
		ans += el*(interval[1] - interval[0] + 2)*(interval[1] - interval[0] + 1)//2
	print(ans)

