# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # dfs solution
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if not root:
                return [True, 0]

            left, leftHeight = dfs(root.left)
            right, rightHeight = dfs(root.right)

            height = 1 + max(leftHeight, rightHeight)

            if abs(rightHeight - leftHeight) > 1:
                return [False, height]

            return [left and right, height]

        return dfs(root)[0]
        
        