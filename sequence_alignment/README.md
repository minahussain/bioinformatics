# Sequence Alignment

## Longest Common Subsequence

### Problem

Given two strings of length m and n, find the longest common subsequence between them.

### LCS

A string of length n has 2^n possible subsequences.. let's not try to compute all of those.

We will align two strings, and try to maximize matches. 
Let X="ABCA", Y = "ADCBA"

	A B C A 
	A D C B A

With no insertions or deletions, we have 2 matches.

	- A B C A
	A D C B A

If we insert a space into X, we can align the last char 'A' but we lost the first one.

	A - B C A
	A D C B A

Lets shift the insertion, now we have the first and last chars match.

	A B - C A
	A D C B A

Obviously, this insertion doesn't improve anything. 

	A B C - A
	A D C B A

There we go, now 'C' aligns and we have our max alignment of 3.

So, what if |Y| < |X| ? Let's swap our previous X and Y

	A D C B A
	A B C - A

The space in our new Y is called a deletion.

**indel**: *in*sertion/*del*etions

Alright so how to program this? We're iterating through both of the strings, matching up chars at different points (think: double loop)

At char i,j for strings X and Y respectively: 
If chars match, we count it, so lcs(i-1, j-1) + 1. 
If no match, we'll try an indel to move that char over, so
lcs(i-1, j), an insertion, or lcs(i, j-1), a deletion. A char doesn't match with a space, so + 0.

This means we need the values [i-1, j-1], [i-1, j], and [i, j-1] precomputed. And sometimes a match doesn't give us the best subsequence, so we would want to choose from the max of those values. 
Then, once at [m, n] we should have the max length of the subsequence (think: 2d matrix)

So lets do a 2d matrix lol

Matches are always on the diagonal, insertions are from above, and deletions are from the left.


```
LCS(X, Y)
	m = |X|
	n = |Y|
	for i = 1 to m
		E[i, 0] = 0
	for j = 1 to n
		E[0, j] = 0
	for i = 1 to m
		for j = 1 to n
			if X[i] == Y[j]: E[i,j] = E[i-1,j-1] + 1, S[i,j] = 'diag'
			elseif E[i-1, j] >= E[i,j-1]: 
				E[i,j] = E[i-1,j]
				S[i,j] = 'above'
			else:
				E[i,j] = E[i,j-1]
				S[i,j] = 'left'
```

To get the alignment, backtrack through S to find the subsequence string, prepending the string along since we start at S[m, n]



