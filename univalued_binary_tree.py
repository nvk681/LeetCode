# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        def pre_order_parsing(node, val):
            if node is None: return True
            if node.val != val:
                return False
            left = pre_order_parsing(node.left, val)
            if left:
                right = pre_order_parsing(node.right, val)
            else:
                return False
            return left and right
        return pre_order_parsing(root, root.val)