Shortest Paths
Time limit: 3000 ms
Memory limit: 128 MB

You are given a directed graph consisting of NN nodes and MM edges and the index of a node, vv. For each node in the graph, uu print the minimum number of edges you must transverse to get from vv to uu, or -1 if uu is unreachable from vv.

Standard input
On the first line of input, you will find 33 integer values, N MNM and vv. Then MM lines follow, each consisting of 22 integers xx and yy, representing one of the MM edges.

Standard output
You should ouput NN integers. The ii-th integer should represent the length of the shortest path from vv to ii.

Restrictions
1 \leq v \leq N \leq 100.0001≤v≤N≤100.000
1 \leq M \leq 1.000.0001≤M≤1.000.000

Input	
5 7 2
1 2
2 1
2 2
3 2
2 5
5 3
4 5
Output
1 0 2 -1 1
