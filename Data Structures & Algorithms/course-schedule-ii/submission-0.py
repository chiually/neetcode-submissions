class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[course].append(pre)

        res = []
        visited = [False] * numCourses # fully processed courses
        cycle = set() # current dfs path

        def dfs(node):

            if node in cycle:
                return False # cycle detected
            if visited[node]:
                return True

            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False

            cycle.remove(node)
            visited[node] = True
            res.append(node)
            return True
                
        
        
        for node in range(numCourses):
            if not visited[node]:
                if not dfs(node):
                    return []
        return res
        
