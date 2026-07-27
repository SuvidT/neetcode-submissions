# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == []:
            return []
 
        def traverse(node: Optional[TreeNode]) -> List[int]:
            if node is not None:
                return traverse(node.left) + traverse(node.right) + [node.val]
            else:
                return []