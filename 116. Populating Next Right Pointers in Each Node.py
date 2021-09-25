"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        q = [root]
        n=1
        while n>0:
            x = 0
            for i in range(n):
                t = q[0]
                q.pop(0)
                if t.left!=None:
                    q.append(t.left)
                    x+=1
                if t.right!=None:
                    q.append(t.right)
                    x+=1
                if i == n-1:
                    t.next = None
                else:
                    t.next = q[0]
            n = x
        return root
                    
