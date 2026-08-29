class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort() # so once sum is greater than target, stop

        def dfs(idx, currList, total):

            if total == target:
                res.append(currList.copy())
                return

            for j in range(idx, len(nums)):

                if total + nums[j] > target:
                    break

                currList.append(nums[j])
                dfs(j, currList, total + nums[j])
                currList.pop() # back track
        dfs(0, [], 0)
        return res
        