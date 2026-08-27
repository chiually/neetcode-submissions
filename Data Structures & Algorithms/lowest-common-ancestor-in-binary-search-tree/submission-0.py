# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # use bst properties: lowest common ancestor must be between p and q

        if not root:
            return None
        
        if root.right and p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.left and p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root