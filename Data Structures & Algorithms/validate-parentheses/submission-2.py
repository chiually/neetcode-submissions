class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "]": "[", "}" : "{"}

        for ch in s:

            if ch in "({[":
                stack.append(ch)
                continue

            if stack == [] or mapping[ch] != stack.pop():
                return False

        return stack == []

        