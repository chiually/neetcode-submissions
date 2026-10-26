class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make the graph
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)

        # determine if cycle in graph
        visit = [0] * numCourses # 0 = unvisited, 1 = visiting, 2 = done
        def dfs(i):

            if visit[i] == 1:
                return True
            if visit[i] == 2:
                return False

            visit[i] = 1

            for nei in adj[i]:
                if dfs(nei):
                    return True

            visit[i] = 2 

        for i in range(numCourses):
            if visit[i] == 0:
                if dfs(i):
                    return False

        return True


        
        