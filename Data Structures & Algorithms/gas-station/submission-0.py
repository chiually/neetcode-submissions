class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # verify solution exists
        if sum(gas) < sum(cost):
            return -1

        # a solution exists we just need to find it
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                start = i + 1
                total = 0
            
        return start
        