class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B , A # A is always smaller list

        # size of left partition of merged list
        half = (len(A) + len(B)) // 2

        l, r = 0, len(A) - 1
        while True: # guaranteed to have median, so can just return it
            mid = (l + r) // 2 # pointer in A
            i = half - mid - 2 # pointer in B
            
            aLeft = A[mid] if mid >= 0 else float("-inf")
            aRight = A[mid + 1] if mid + 1 < len(A) else float("inf")
            bLeft = B[i] if i >= 0 else float("-inf")
            bRight = B[i + 1] if i + 1 < len(B) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                # odd
                if (len(A) + len(B)) % 2 == 1:
                    return min(aRight, bRight)
                # even
                start, end = min(aRight, bRight), max(aLeft, bLeft)
                return (start + end) / 2

            elif aLeft > bRight:
                r = mid - 1
            else:
                l = mid + 1
