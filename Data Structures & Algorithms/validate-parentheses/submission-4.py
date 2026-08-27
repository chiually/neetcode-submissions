class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {")": "(", "]": "[", "}" : "{"}

        for char in s:

            if char in "({[":
                stack.append(char)
            elif char in ")}]":

                if not stack or mapping[char] != stack.pop():
                    return False

            print(stack)

        return stack == []