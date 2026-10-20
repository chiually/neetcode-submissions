import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        vals = list(freq.keys())
        vals.sort(key=lambda num: freq[num])

        return vals[-k:]


        