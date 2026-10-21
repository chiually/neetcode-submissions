# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder: root left right
        # inorder : left root right

        # prework
        pos = {}
        for i in range(len(inorder)):
            pos[inorder[i]] = i

        root_idx = 0
        def dfs(l, r):
            if l > r:
                return

            nonlocal root_idx

            val = preorder[root_idx]
            root = TreeNode(val)
            root_idx += 1

            # get position of root in inorder list
            mid = pos[val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        # go through inorder until hit root: inorder list for left subtree
        
        return dfs(0, len(inorder) - 1)