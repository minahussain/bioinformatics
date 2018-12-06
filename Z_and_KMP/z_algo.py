def toString(Arr):
	s = ''
	for elem in Arr:
		s += str(elem) + ' '
	return s

def z_naive(S):
	Z = [0] * len(S)				# store z values
	count = 0

	for i in range(len(S)):			
		s_i = S[i:]
		for j in range(len(s_i)):	
			count = j
			if s_i[j] != S[j]:		# match S and substring
				break
		Z[i] = count
	return toString(Z)

def z_value(S, s):
	count = 0
	n = len(s)
	if n == 1 and s[0] == S[0]: 
		count = 1
	else:
		for i in range(n):
			count = i
			if s[i] != S[i]: break
	return count

def z_efficient(S):
	Z = [0] * len(S)
	k = 0 			
	rt = lt = 0 	# z box right and left border index
	Z[0] = len(S)

	for i in range(1,len(S)):
		if i > rt:
			# outside z box, calcuate z value
			Z[i] = z_value(S, S[i:])
			lt = i
			rt = i + Z[i]-1
		else:
			p = i - lt 				# matched char's position	
			if Z[p] <= rt - i + 1:	# matched z value within box
				Z[i] = Z[p]
			else:
				# check if chars outside box match
				for j in range(rt+1, len(S)):
					if S[j] == S[j-i]:
						Z[j] = i-j
						lt = i
						rt = j-1
						break
	return toString(Z)


if __name__ == "__main__":
	print(z_efficient("ABABXABABYABACA"))

