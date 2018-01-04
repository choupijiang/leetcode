# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or (root.left is None and root.right is None):
            return root
        temp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = temp
        return root

