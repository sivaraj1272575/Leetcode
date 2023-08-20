# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if root == None:
            return [[""]]
        def getHeight(root):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 0
            return max(getHeight(root.left), getHeight(root.right)) + 1
        n = getHeight(root)
        cols = 2**(n+1)-1
        ans = [['']*cols for _ in range(n+1)]

        ans[0][cols//2] = str(root.val)
        q = [(root, 0, cols//2)]
        while q:
            # size = len(q)
            # for i in range(size):
            node, r, c = q.pop(0)
            if node.left:
                nr, nc = r+1, c-(2**(n-r-1))
                q.append((node.left, nr, nc))
                ans[nr][nc] = str(node.left.val)
            if node.right:
                nr, nc = r+1, c+(2**(n-r-1))
                q.append((node.right, nr, nc))
                ans[nr][nc] = str(node.right.val)


        return ans
