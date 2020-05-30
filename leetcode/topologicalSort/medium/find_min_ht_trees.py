"""
310 min ht trees

https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts


High level idea is to keep pruning the outer node which has zero or one edge from the tree. Since it's a undircted graph, the only edge allowed for a outer node is the edge connect it with an inner node.
Those last left nodes are at the "center" of the tree so expand from them, the tree will have minimal height.
So in each iteration, we search those outer nodes. In each iteration, we prune those outer node by removing any edge that involves them. Thus, it's kind of a topological sort.
Eventually, if next queue for next iteration is empty, current queue contains those center nodes.
"""

def findMinHeightTrees(self, n, edges):
    if n == 1: return [0]
    adj = [set() for _ in xrange(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)

    leaves = [i for i in xrange(n) if len(adj[i]) == 1]

    while n > 2:
        n -= len(leaves)
        newLeaves = []
        for i in leaves:
            j = adj[i].pop()
            adj[j].remove(i)
            if len(adj[j]) == 1: newLeaves.append(j)
        leaves = newLeaves
    return leaves
