# Z Algorithm

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

## Efficient Idea

Notice how the algorithm is inefficent when we have repeated matched characters that we've already compared. What if we can somehow remember the values of matched chars?

### Z box

For example, S="abaacababaa"
At position 5, we compare up to 'abab' and see that 'aba' matches the prefix. Let's make 'aba' from i=5 to i=7, our current box of matched chars.

At position 6, we've moved one spot in our box, so this char must match S[1] in the prefix. 

**Does this mean Z[6] equals Z[1] ?**

Currently, we are in the middle of our box. If Z[1] = 0, and S[6] equals S[1], then it must be a char that does not match the prefix, and thus Z[6] = Z[1] = 0. 
However, if Z[1] > 0, then the prefix must match the substring at S[6] at least until the end of our box. If it matched more chars outside our box, then our box would be longer. **Think about this**

At position 7, we are at the end of the box. The pair match z value is 1 (Z[2] = 1). However, we have the substring 'abaa' starting at S[7], so Z[7] must be 4. *At the end of the box, we must do new comparisons to figure out our Z value*, because we have not compared further chars to know if it'll have the same z value.


```
def z_efficient(S):
	Z = [0] * len(S)		
	rt = lt = 0 						# z box right and left border index
	Z[0] = len(S)

	for i in range(1,len(S)):
		if i > rt:						# outside Z box, naive
			Z[i] = z_value(S, S[i:])		
			lt = i
			rt = i + Z[i]-1
		else:							# inside Z box, use Z value pair
			p = i - lt 					
			if Z[p] < rt - i + 1:
				Z[i] = Z[p]
			else:						# end Z box, naive
				j = rt + 1
				while j < len(S) and S[j] == S[j - i]:
					j += 1
				Z[i] = j - i
				lt = i
				rt = j - 1
	return toString(Z)
```




