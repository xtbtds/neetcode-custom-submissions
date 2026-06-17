class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, a):
        if self.parents[a] == a:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        ar = self.find(a)
        br = self.find(b)
        if ar == br:
            return False
        if self.size[ar] < self.size[br]:
            ar, br = br, ar
        self.parents[br] = ar
        self.size[ar] += self.size[br]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a, b in edges:
            res = dsu.union(a, b)
            if res:
                n-=1
        return n


