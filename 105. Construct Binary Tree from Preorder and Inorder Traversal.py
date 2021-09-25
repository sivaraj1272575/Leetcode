# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preindex = 0
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
        
        def getTree(preorder,inorder,inorder_start,inorder_end):
            if inorder_start > inorder_end:
                return None
            nonlocal preindex
            newnode = getNode(preorder[preindex])
            preindex +=1
            
            if inorder_start == inorder_end:
                return newnode
            
            sch = search(inorder,inorder_start,inorder_end,newnode.val)
            newnode.left = getTree(preorder,inorder,inorder_start,sch-1)
            newnode.right = getTree(preorder,inorder,sch+1,inorder_end)
            return newnode
        
        return getTree(preorder,inorder,0,len(inorder)-1)
