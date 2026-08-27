# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        s = ""

        def dfs(node):
            nonlocal s

            if not node:
                s = s + 'null' + "#"
                return 

            s = s + str(node.val) + "#"

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        tree = data.split('#')

        if tree[0] == 'null':
            return None

        idx = 0
        def dfs():
            nonlocal idx
            if tree[idx] == 'null' or tree[idx] == '':
                idx += 1
                return None

            node = TreeNode(tree[idx])
            idx += 1 # must be called right after

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
