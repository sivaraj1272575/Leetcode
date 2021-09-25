# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        postindex = len(postorder)-1
        def getNode(n):
            t = TreeNode()
            t.val = n
            t.left = None
            t.right = None
            return t
        def search(array,start,end,value):
            for i in range(start,end+1):
                if array[i] == value:
                    return i
        def getTree(inorder,postorder,in_start,in_end):
            if in_start>in_end:
                return None
            nonlocal postindex
            newnode = getNode(postorder[postindex])
            postindex -= 1
            if in_start == in_end:
                return newnode
            sch = search(inorder,in_start,in_end,newnode.val)
            newnode.right = getTree(inorder,postorder,sch+1,in_end)
            newnode.left = getTree(inorder,postorder,in_start,sch-1) 
            return newnode
        
        return getTree(inorder,postorder,0,len(inorder)-1)
