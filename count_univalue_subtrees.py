# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root) -> int:
        if root is None: return 0
        self.global_count = 0
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
        def parse_all_nodes(node):
            if node is not None:
                if pre_order_parsing(node, node.val):
                    self.global_count += 1
                if node.left is not None:
                    parse_all_nodes(node.left)
                if node.right is not None:
                    parse_all_nodes(node.right)
        parse_all_nodes(root)
        return self.global_count