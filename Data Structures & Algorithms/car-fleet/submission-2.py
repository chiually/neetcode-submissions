import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # create a list of (position, speed) tuples
        pairs = [(position[i], speed[i]) for i in range(len(position))]

        # sort by position
        pairs.sort()

        stack = []

        # go through list in reverse
        for i in range(len(pairs) - 1, -1, -1):
            p, s = pairs[i]
            
            # calc when car reaches dest
            time = (target - p) / s

            # if car is not in same fleet as last item on stack
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)