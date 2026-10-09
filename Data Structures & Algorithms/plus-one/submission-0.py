class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        digits[n - 1] += 1
        carry = 0

        for i in range(n - 1, -1, -1):
            val = carry + digits[i]
            carry = 0

            if val == 10:
                carry = 1
                val = 0

            digits[i] = val

        if carry == 1:
            digits.insert(0, 1)

        return digits

            
        