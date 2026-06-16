class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [set() for i in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neigh in adj[node]:
                if neigh != parent:
                    if not dfs(neigh, node):
                        return False
            return True

        return dfs(0, -1) and len(visited)==n
            
    # def validTree(self, n: int, edges: List[List[int]]) -> bool:
    #     if len(edges) != n-1:
    #         return False
    #     adj = [set() for i in range(n)]
    #     for a, b in edges:
    #         adj[a].add(b)
    #         adj[b].add(a)
    #     visited = set()
    #     def dfs(node):
    #         if node in visited:
    #             return
    #         visited.add(node)
    #         for neigh in adj[node]:
    #             dfs(neigh)
    #     dfs(0)
    #     return len(visited)==n
