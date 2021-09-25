# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(node,low,high):
            if node == None:
                return True
            if high!=None and node.val>=high:
                return False
            if low!=None and node.val<=low:
                return False
            return check(node.left,low,node.val) and check(node.right,node.val,high)
        
        
        return check(root,None,None)
