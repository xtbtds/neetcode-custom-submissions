class DSU:
    def __init__(self, n):
        self.comps = n
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, elem):
        if self.parents[elem] == elem:
            return elem
        self.parents[elem] = self.find(self.parents[elem])
        return self.parents[elem]

    def union(self, a, b):
        a_repr = self.find(a)
        b_repr = self.find(b)
        if a_repr == b_repr:
            return False
        if self.size[a_repr] > self.size[b_repr]:
            a_repr, b_repr = b_repr, a_repr
        self.parents[b_repr] = a_repr
        self.size[a_repr] += self.size[b_repr]
        return True
        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        dsu = DSU(n)
        for a, b, in edges:
            print(n)
            union_res = dsu.union(a, b)
            if union_res:
                n-=1
            else:
                return False
        return n == 1


        