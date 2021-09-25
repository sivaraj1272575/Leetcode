# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:    
        if root==None:
            return []
        q = []
        ans=[]
        q.append([root])
        n = 1
        ch = 0
        while len(q)>0:
            temp = []
            child = []
            if ch == 0:
                for i in q[0]:
                    temp.append(i.val)
                    if i.left!=None:
                        child.append(i.left)
                    if i.right!=None:
                        child.append(i.right)
                q.pop(0)
            else:
                for i in q[0]:
                    if i.left!=None:
                        child.append(i.left)
                    if i.right!=None:
                        child.append(i.right)
                for i in reversed(q[0]):
                    temp.append(i.val)
                q.pop(0)
            ans.append(temp.copy())
            if len(child)>0:
                q.append(child.copy())
            ch = (ch+1)%2
        print(ans)
        return ans
        
