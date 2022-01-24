# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def find_and_remove_leaf(root):
    temp = []
    if root.left is None and root.right is None:
        val = root.val
        root = None
        return [val]
    if root.left is not None:
        temp.append(find_and_remove_leaf(root.left)[0])
        if root.left.right is None and root.left.right is None:
            root.left = None
    if root.right is not None: 
        temp.append(find_and_remove_leaf(root.right)[0])
        if root.right.right is None and root.right.left is None:
            root.right = None
    return temp
    
# class Solution:
def findLeaves(root):
    list_of_removals = []
    while root is not None:
        list_of_removals.append(find_and_remove_leaf(root))
    return list_of_removals
        