class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top K --> heaps!
        
        # create hash map of num to freq
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # build list of (freq, num) pairs
        arr = []
        for key, v in count.items():
            arr.append([v, key])
        arr.sort() # checks index 0 first, so sorted by ascending freq

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
            

        

        