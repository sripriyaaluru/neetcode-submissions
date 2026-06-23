class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #cycle detection: dfs undirected
        if len(edges)>(n-1):
            return False
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visiting=set()
        def dfs(node,par):
            if node in visiting:
                return False
            visiting.add(node)
            for n in adj[node]:
                if n==par:
                    continue
                if not dfs(n,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visiting)==n








