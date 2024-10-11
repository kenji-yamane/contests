# x y z
#   y z c -> repeated pair -> check if i - 1 and i + 3 are different -> then yes
# x y z
#     z a b -> repeated pair of pairs

# 2 2

# x y z
#        x y a -> repeated pair of pairs

# 3 2 2 2 2 5

def hash_pair(arr):
	return arr[0]*10**6 + arr[1]

def hash_triple(arr):
	return arr[0]*10**12 + arr[1]*10**6 + arr[2]

def hash_arr(arr):
	if len(arr) == 2:
		return hash_pair(arr)
	else:
		return hash_triple(arr)

def match(arr):
	frequencies = {}
	for el in arr:
		hash_key = hash_arr(el)
		if hash_key not in frequencies:
			frequencies[hash_key] = 0
		frequencies[hash_key] += 1

	ans = 0
	for key, count in frequencies.items():
		if count > 1:
			ans += count*(count - 1)//2
	return ans

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	triples = []
	for i in range(len(a) - 2):
		triples.append([a[i], a[i + 1], a[i + 2]])
	middle_pairs = []
	for i in range(len(a) - 2):
		middle_pairs.append([a[i], a[i + 2]])
	left_pairs = []
	for i in range(len(a) - 2):
		left_pairs.append([a[i], a[i + 1]])
	right_pairs = []
	for i in range(1, len(a) - 1):
		right_pairs.append([a[i], a[i + 1]])

	print(match(middle_pairs) + match(left_pairs) + match(right_pairs) - 3*match(triples))

