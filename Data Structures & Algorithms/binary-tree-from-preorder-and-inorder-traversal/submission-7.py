# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # preorder: root left right
        # inorder: left root right
        
        pos = {val: i for i, val in enumerate(inorder)} # position of root in inorder list
        preIndex = 0

        def dfs(l, r):
            nonlocal preIndex

            if preIndex >= len(preorder) or l > r:
                return

            val = preorder[preIndex]
            root = TreeNode(val)
            preIndex += 1

            root.left = dfs(l, pos[val] - 1)
            root.right = dfs(pos[val] + 1, r)

            return root

        return dfs(0, len(preorder) - 1)