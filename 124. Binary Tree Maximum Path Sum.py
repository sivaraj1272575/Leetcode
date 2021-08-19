class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -1000000
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            a = max(max(left, right)+root.val, root.val)
            b = max(a, left+right+root.val)
            self.ans = max(self.ans, b)
            
            return a
        dfs(root)
        return self.ans
