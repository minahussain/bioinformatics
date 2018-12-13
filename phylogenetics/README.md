# Phylogenetics

## Distance-Based Phylogeny Problem

### Problem

Reconstruct an evolutionary tree fitting distance matrix *D*

A distance matrix is
1. Symmetric
2. Non-negative
3. satifies triangle's inequality: $D_{i,j} + D_{j,k} \geq D_{i,k}$

### Additive Phylogeny

**limb length**: length of the limb connecting leaf *j* to its parent in the tree of *D*

For each *j*, compute limb_length(*j*) by finding the min over all pairs of leaves *i* and *k*

- pick leaf *j*, compute limb_length(*j*), construct matrix *D^{trim}*
- solve Distance-Based Phylogeny problem for *D^{trim}*
- identitfy point *p* where leaf *j* should be attached in tree of *D*
- add limb of length limb_length(*j*) at *p* in tree of *D^{trim}* to form tree of *D*

```
ADDITIVEPHYLOGENY(D, n)
	if n = 2
		return the tree consisting of a single edge of length D[1,2]

	limbLen = LIMB(D, n)
	for j = 1 to n− 1
		D[j,n] = D[j,n] − limbLen
		D[n,j] = D[j,n]
	(i, n, k) = three leaves such that D[i,k] = D[i,n] + D[n,k]
	x = Di,n
	remove row n and column n from D
	T = ADDITIVEPHYLOGENY(D, n− 1)
	v = the node in T at distance x from i on the path between i and k
	add leaf n back to T by creating a limb (v, n) of length limbLen
	return T
```


### Ultrametric Evolutionary Trees

UPGMA (*Unweighted Pair Group Method with Arithmetic Mean*) works on non-additive distance matrices, unlike Additive Phylogeny.

Assumes an **ultrametric tree**: distances from the root to every branch tip are equal 

However, UPGMA merges two leaves using min distance in *D*. 
**The min value in the distance matrix is NOT always neighboring leaves**

1. Build pairwise distance matrix
2. Cluster a pair of sequences closest to each other, create internal node that has the sequences as children
$$
	D(cl_{1},cl_{2}) = \frac{1}{\abs{cl_{1}}\abs{cl_{2}}} \sum_{p \in cl_{1},q \in cl_{2}}{D(p,q)}
$$
3. Repeat, include newly created internal nodes in the distance matrix

### Neighbor Joining Algorithm

Transform *D* into a matrix where the min value corresponds to neighboring leaves. Define $TotalDistance_{D}(i) = \sum_{1\leq k \leq n}{D_{i,k}}$


## Small Parsimony Problem

### Small Parsimony in Rooted Tree

**parsimony score**: sum of the lengths of its edges

Find the most parsimonious labeling of the internal nodes of a rooted tree

Need to know the evolutionary tree in advance.

### Small Parsimony in Unrooted Tree

## Large Parsimony Problem

