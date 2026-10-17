# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        nodes = []

        # root always in right side view
        nodes.append(root.val)

        # get ride side view of right subtree
        rightNodes, rightHeight = self.getRightSideView(root.right, 0)
        nodes += rightNodes

        # get rightside view after a certain depth reached
        leftNodes, leftHeight = self.getRightSideView(root.left, rightHeight)
        nodes += leftNodes

        return nodes

    # helper function that gets the right side view after certain height reached
    def getRightSideView(self, root: Optional[TreeNode], height: int) -> tuple[List[int], int]:
        
        if not root:
            return [], 0
        nodes = []

        if height <= 0:
            nodes.append(root.val)

        # get ride side view of children
        rightNodes, rightHeight = self.getRightSideView(root.right, height - 1)
        nodes += rightNodes

        leftNodes, leftHeight = self.getRightSideView(root.left, max(rightHeight, height - 1))
        nodes += leftNodes
        print(leftNodes)

        # return list of nodes and height of tree 
        return nodes, max(rightHeight, leftHeight) + 1
        
