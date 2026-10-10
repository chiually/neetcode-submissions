class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        n = len(temperatures)

        res = [0] * n
        for i in range(n):
                
            while stack and stack[-1] < temperatures[i]:
                stack.pop()
                idx = stack.pop()
                val = i - idx
                
                res[idx] = val
            
            # add curr temperature to the stack
            stack.append(i)
            stack.append(temperatures[i])

        return res


        