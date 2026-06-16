class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        global_vis = set()
        def dfs(node):
            global_vis.add(node)
            for ne in adj[node]:
                if ne not in global_vis:
                    dfs(ne)
        res = 0
        for node in range(n):
            if node in global_vis:
                continue
            res+=1
            dfs(node)
        return res