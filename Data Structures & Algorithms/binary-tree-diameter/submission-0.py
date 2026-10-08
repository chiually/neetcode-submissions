# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0 # longest path between any two nodes so height of left and right subtree

        # note: to avoid nonlocal variable 
        def dfs(root):
            nonlocal diameter

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            diameter = max(diameter, left + right)
            return 1 + max(left, right)

            
        dfs(root)
        return diameter
        