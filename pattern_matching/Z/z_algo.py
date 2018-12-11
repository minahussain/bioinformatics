import unittest

def toString(Arr):
	s = ''
	for elem in Arr:
		s += str(elem) + ' '
	return s[:-1]

def z_naive(S):
	Z = [0] * len(S)

	for i in range(len(S)):			
		s_i = S[i:]
		j = 0
		
		# parse each substring at i
		while j < len(s_i) and s_i[j] == S[j]:
			j += 1
		Z[i] = j
	return toString(Z)

def z_value(S, s):
	i = 0
	while i < len(s) and s[i] == S[i]:
		i += 1
	return i

def z_efficient(S):
	Z = [0] * len(S)		
	rt = lt = 0 						# Z box right and left index
	Z[0] = len(S)

	for i in range(1,len(S)):
		if i > rt:						# outside Z box, new comparisons
			Z[i] = z_value(S, S[i:])		# naive computation
			lt = i
			rt = i + Z[i]-1
		else:							# inside Z box, use Z value pair
			p = i - lt 					
			if Z[p] < rt - i + 1:
				Z[i] = Z[p]
			else:						# end Z box, new comparisons
				j = rt + 1
				while j < len(S) and S[j] == S[j - i]:
					j += 1
				Z[i] = j - i
				lt = i
				rt = j - 1
	return toString(Z)


class TestZAlgo(unittest.TestCase):
	def test_naive(self):
		self.assertEqual('15 0 2 0 0 4 0 2 0 0 3 0 1 0 1', z_naive('ABABXABABYABACA'))
		self.assertEqual('11 0 1 1 0 3 0 4 0 1 1', z_naive('abaacababaa'))
	def test_efficient(self):
		self.assertEqual('15 0 2 0 0 4 0 2 0 0 3 0 1 0 1', z_efficient('ABABXABABYABACA'))
		self.assertEqual('11 0 1 1 0 3 0 4 0 1 1', z_efficient('abaacababaa'))


if __name__ == "__main__":
	unittest.main()


