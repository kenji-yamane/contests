def read_numbers():
	line = input().strip().split(' ')
	line = [int(i) for i in line]
	return line

t = int(input())

for _ in range(t):
	threadlets = read_numbers()
	threadlets.sort()
	ops = 0
	while len(set(threadlets)) > 1 and ops < 3:
		unique_threads = list(set(threadlets))
		unique_threads.sort()
		threadlets[-1] = unique_threads[-2]
		threadlets.append(unique_threads[-1] - unique_threads[-2])
		threadlets.sort()
		ops += 1
	if len(set(threadlets)) == 1:
		print('yes')
	else:
		print('no')

