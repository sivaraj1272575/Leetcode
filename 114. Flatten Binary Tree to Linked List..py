# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(root):
            if root == None:
                return 
            if root.left == None and root.right == None:
                return 
            
            preorder(root.left)
            if root.left!=None:
                
                temp = root.right
                root.right = root.left
                root.left = None
                t1 = root.right
                while t1.right!=None:
                    t1 = t1.right
                t1.right = temp
            preorder(root.right)
            
        preorder(root)
