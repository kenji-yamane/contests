def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def sum_arr(a, b):
	for i in range(len(a)):
		a[i] += b[i]

t = int(input())

for _ in range(t):
	n = int(input())
	s = input().strip()

	last_even = [0]*26
	last_odd = [0]*26
	for i in range(len(s) - 1, -1, -1):
		if i%2 == 0:
			last_even[ord(s[i]) - ord('a')] += 1
		else:
			last_odd[ord(s[i]) - ord('a')] += 1
	if len(s)%2 == 0:
		print(len(s) - max(last_even) - max(last_odd))
		continue

	first_even = [0]*26
	first_odd = [0]*26
	ans = len(s)
	for i in range(len(s)):
		if i%2 == 0:
			last_even[ord(s[i]) - ord('a')] -= 1
		else:
			last_odd[ord(s[i]) - ord('a')] -= 1

		even = [0]*26
		odd = [0]*26
		if i > 0:
			if (i - 1)%2 == 0:
				sum_arr(even, first_even)
			else:
				sum_arr(even, first_odd)
		if i > 1:
			if (i - 2)%2 == 0:
				sum_arr(odd, first_even)
			else:
				sum_arr(odd, first_odd)
		if i < len(s) - 1:
			if (i + 1)%2 == 0:
				sum_arr(odd, last_even)
			else:
				sum_arr(odd, last_odd)
		if i < len(s) - 2:
			if (i + 2)%2 == 0:
				sum_arr(even, last_even)
			else:
				sum_arr(even, last_odd)
		ans = min(ans, len(s) - max(even) - max(odd))

		if i%2 == 0:
			first_even[ord(s[i]) - ord('a')] += 1
		else:
			first_odd[ord(s[i]) - ord('a')] += 1
	print(ans)

