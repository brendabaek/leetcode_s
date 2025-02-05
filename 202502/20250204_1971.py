## https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination : return True
        graph = {i : [] for i in range(n)}
        for i, j in edges :
            graph[i].append(j)
            graph[j].append(i)

        def dfs(node, visited) :
            if node == destination : return True
            visited.add(node)
            for n in graph[node] :
                if n not in visited :
                    if dfs(n, visited) == True : return True
            return False
        
        visited = set()
        return dfs(source, visited)