# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # do ordered traversal and build list
        elements = []

        def dfs(root):

            if not root:
                return

            dfs(root.left)
            elements.append(root.val)
            dfs(root.right)


        dfs(root)

        # index the kth element
        return elements[k - 1]
        