# Z Algorithm

Z and KMP algorithm concepts.

### Z Algorithm

## Naive Idea

We want to find all occurrences of a pattern in a string. We can iterate through the string, for i = 1 to n, and match each substring beginning at i with the beginning of the entire string. 

```
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

```

What will happen if we pass S="aaaaaa" ? 
Each substring's character will be compared: n + (n-1) + ... + 2 + 1 times, running in n² time.

Notice how the algorithm is inefficent when we can see repeated letters. Instead, we can remember what we've seen using the idea of a Z-box.

For example, S="abaacababaa"
When at position 5, we compare up to 'abab' and see that 'aba' matches the prefix. Let's make 'aba' from i=5 to i=7, our current box.

At position 6, we've moved one spot in our box, so this position must match S[1] in the prefix. THINK: Does this mean Z[6] equals Z[1] ?

At i=6, we are in the middle of the box. If Z[1] = 0, then S[4] must be a char that does not match the prefix. If Z[1] > 0, then the prefix must match the substring at S[4] at least until the end of our box. If it matched more, then the box would be longer.

At i=7, we are at the end of the box. The prefix Z[2] = 1. However, at S[7], we match 'abaa,' so Z[7] = 4. At the end of the box, we must do new comparisons to figure out our Z value. 


```
def z_efficient(S):
	Z = [0] * len(S)		
	rt = lt = 0 	# z box right and left border index
	Z[0] = len(S)

	for i in range(1,len(S)):
		if i > rt:						# outside Z box, new comparisons
			Z[i] = z_value(S, S[i:])	# naive computation
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
```




