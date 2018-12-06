# Z Algorithm and KMP

Z and KMP algorithm concepts.

### Z Algorithm

## Idea

We want to find all occurrences of a pattern in a string. Naively, we can iterate through the string, for i = 1 to n, and match each substring beginning at i with the beginning of the entire string. 

```
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

```

However, what will happen if we pass S="aaaaaa" ? 
Each substring's character will be compared: n + (n-1) + ... + 1 times, running in n² time.

Instead, let's think of how we can reduce this.

```
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
```




