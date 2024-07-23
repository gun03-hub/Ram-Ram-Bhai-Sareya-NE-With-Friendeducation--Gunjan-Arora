#P1- Reorder Routesto Make All Paths Leads to the City Zero
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        
        visited = [False] * n
        self.ans = 0
        
        def dfs(node, parent):
            visited[node] = True
            for neighbor, direction in graph[node]:
                if neighbor != parent:
                    if direction == 1:
                        self.ans += 1
                    if not visited[neighbor]:
                        dfs(neighbor, node)
        
        dfs(0, -1)
        return self.ans
#P2- Evaluate Division
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for (a, b), v in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = v
            graph[b][a] = 1 / v
        
        def dfs(a, b, visited):
            if a not in graph or b not in graph:
                return -1.0
            if b in graph[a]:
                return graph[a][b]
            for c in graph[a]:
                if c not in visited:
                    visited.add(c)
                    v = dfs(c, b, visited)
                    if v != -1.0:
                        return graph[a][c] * v
            return -1.0
        
        return [dfs(a, b, set()) for a, b in queries]
