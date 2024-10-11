# 1 3
# 0 1
# 2 3
# 3 + 3 + 3 + 3 + 4
# 16

# 1 3
# 0 2
# 2 4
# 20

# 0 3

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def mexes(sequence):
	visited = [False]*(len(sequence) + 2)
	for el in sequence:
		if el < len(sequence) + 2:
			visited[el] = True
	ans = []
	for idx in range(len(visited)):
		if not visited[idx]:
			ans.append(idx)
		if len(ans) == 2:
			break
	return ans

t = int(input())

for _ in range(t):
	n, m = read_line()
	l = []
	sequences = []
	for _ in range(n):
		sequence = read_line()
		l.append(sequence[0])
		sequences.append(sequence[1:])

	optimal = max([max(mexes(sequence)) for sequence in sequences])
	ans = optimal*(min(m, optimal) + 1)
	if m > optimal:
		ans += (m + optimal + 1)*(m - optimal)//2
	print(ans)

