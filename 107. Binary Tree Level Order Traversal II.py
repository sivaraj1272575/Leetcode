# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        n = 1
        q = [root]
        ans = []
        while n>0:
            temp = []
            x = 0
            for i in range(n):
                t = q[0]
                temp.append(t.val)
                q.pop(0)
                if t.left!=None:
                    q.append(t.left)
                    x+=1
                if t.right!=None:
                    q.append(t.right)
                    x+=1
            n = x
            ans.append(temp.copy())
        l = 0
        h = len(ans)-1
        while l<h:
            t = ans[l]
            ans[l] = ans[h]
            ans[h] = t
            l+=1
            h-=1
        return ans
