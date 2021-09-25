# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root, temp, sm):
            if root == None:
                return
            if root.left == None and root.right == None and sm+root.val == targetSum:
                ans.append(temp.copy()+[root.val])
            dfs(root.left, temp+[root.val], sm+root.val)
            dfs(root.right, temp+[root.val], sm+root.val)
                
        
        dfs(root, [], 0)
        return ans
            
