# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # top down solution
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getHeight(root):
            if not root:
                return 0
            return max(getHeight(root.right) + 1, getHeight(root.left) + 1)

        if not root:
            return True
        # get height of the right and left subtrees
        l, r = getHeight(root.left), getHeight(root.right)

        # if difference is greater than 1 return False
        if abs(l - r) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

        
