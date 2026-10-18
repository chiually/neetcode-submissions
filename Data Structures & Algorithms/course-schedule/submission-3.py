class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make graph
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[course].append(pre)

        # use dfs for cycle detection
        path = set()
        def dfs(course):
            if course in path:
                return True # found cycle

            path.add(course)
            for nei in adj[course]:
                if dfs(nei):
                    return True

            path.remove(course)   
            adj[course] = [] # no cycle from this ode possible
            return False

        for i in range(numCourses):
            if i not in path:
                if dfs(i):
                    return False

        return True
                
                
        