# Clustering

## K-Center Clustering

given a set of data points, find k centers minimizing the max distance between the points and centers

Minimizes **max distance**, outliers will cluster

## K-Means Clustering

given a set of data points, find k center points minimizing the squared error distribution, the mean squared sistance from each point to its nearest center.

Minimizes **center of gravity**, outliers have less weight to become a cluster

### Lloyd's Algorithm

For k-means clustering

1. Choose k arbitrary points as centers
2. **Centers to Clusters**: assign each point to its nearest center
3. **Clusters to Centers**: assign the center of gravity of each cluster as centers
4. Repeat 2 and 3 until centers stop changing, which means the squared error distribution stops decreasing

For each iteration, the squared error distribution can only decrease. Points are assigned to a cluster only if it is closest to it. A cluster's center only changes if its center of gravity has changed among its assigned close points. 

### Downfalls of K-means

Lloyd's Algorithm may result in an 'incorrect' clustering depending on the initial centers chosen. For example, dataset with 3 distinct clumps but we set k=4, then one clump has 2 centers. Another example, below 'o' is a cluster that gets no points assigned to it since it is blocked by surrounding centers.

> .
. o .
  .

### K-means++ Initalizer

We'd like to choose random spread out points as our initial centers. The k-means++ initializer does this by randomly choosing k points, but with each iteration, the probability of a point being chosen is its squared distance from the previously chosen centers.

We aren't choosing the furthest point every iteration, there is still some randomization.

## Soft K-Means Clustering

Helps us deal with **midpoints** amond clusters.
Assign each point k numbers representing the point’s percentage ("responsibility") of each cluster, using expectation maximization

1. Choose random centers
2. Centers to Soft Clusters **E Step**: assign each point a 'responsibility' for each cluster
3. Soft Clusters to Centers **M Step**: assign new centers
