class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # prerequisites are directed edges, if revist a node then return false (cycle detected)

        # build graph of course to pre-requisites
        mapping = {i: [] for i in range(numCourses)}
        for c, pre in prerequisites:
            mapping[c].append(pre)

        visited = set()

        def dfs(course, visited):

            if course in visited:
                return False
            if mapping[course] == []:
                return True

            visited.add(course)
            for pre in mapping[course]:
                if not dfs(pre, visited):
                    return False
            visited.remove(course)
            mapping[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c, visited):
                return False

        return True




        
        