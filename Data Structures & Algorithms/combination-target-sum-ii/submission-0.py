class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        
        res = []
        curr = []

        def dfs(i):
            total = sum(curr)
            
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates):
                return

            
            if total <= target:
                curr.append(candidates[i])
                dfs(i + 1)
                curr.pop()
                # skip duplicates
                while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                    i += 1
                dfs(i + 1)

        dfs(0)
        return res