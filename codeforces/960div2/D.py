# every line that has more than 4 black cells should be dyed with row
# every isolated line in the first column should be dyed with row
# every square operation needs to start at an even numbered column
# given third assumption, every isolated line in the third column should be dyed row

# 0 0  1 0  1 1  0 0  1 0  1 1  0 0  1 0  1 1
# 0 0  0 0  0 0  1 0  1 0  1 0  1 1  1 1  1 1

def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

def dye_long_rows(a):
	operations = 0
	for idx in range(len(a)):
		if a[idx] > 4:
			a[idx] = 0
			operations += 1
	return operations

def state_to_idx(bottom, top):
	if bottom and top:
		return 0
	elif bottom and not top:
		return 1
	elif not bottom and top:
		return 2
	else:
		return 3

def idx_to_state(idx):
	if idx == 0:
		return True, True
	elif idx == 1:
		return True, False
	elif idx == 2:
		return False, True
	elif idx == 3:
		return False, False

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	operations = dye_long_rows(a)

	optimal_op = [[n + 1]*4 for i in range(n + 1)]
	optimal_op[0][state_to_idx(False, False)] = 0

	for a_idx in range(n):
		for state_idx in range(4):
			curr_op = optimal_op[a_idx][state_idx]
			if curr_op == n + 1:
				continue

			bottom, top = idx_to_state(state_idx)
			noop = [a_idx + 1, state_to_idx(False, False)]
			if a[a_idx] == 0 or (bottom and a[a_idx] <= 2):
				optimal_op[noop[0]][noop[1]] = min(curr_op, optimal_op[noop[0]][noop[1]])

			topop = [a_idx + 1, state_to_idx(False, True)]
			if bottom:
				optimal_op[topop[0]][topop[1]] = min(curr_op + 1, optimal_op[topop[0]][topop[1]])

			botop = [a_idx + 1, state_to_idx(True, False)]
			if a[a_idx] <= 2 or top:
				optimal_op[botop[0]][botop[1]] = min(curr_op + 1, optimal_op[botop[0]][botop[1]])

			rowop = [a_idx + 1, state_to_idx(False, False)]
			sqrdop = [a_idx + 2, state_to_idx(False, False)]
			optimal_op[rowop[0]][rowop[1]] = min(curr_op + 1, optimal_op[rowop[0]][rowop[1]])
			if sqrdop[0] < n + 1:
				optimal_op[sqrdop[0]][sqrdop[1]] = min(curr_op + 2, optimal_op[sqrdop[0]][sqrdop[1]])
	print(operations + min(optimal_op[-1]))

