# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getNode(x):
            t = TreeNode(x)
            t.val = x
            return t
        
        def createTree(arr,low,high):
            if low>high:
                return None
            mid = (low+high)//2
            node = getNode(arr[mid])
            node.left = createTree(arr,low,mid-1)
            node.right = createTree(arr,mid+1,high)
            return node
        
            
        arr = []
        temp = head
        while temp!=None:
            arr.append(temp.val)
            temp = temp.next
        return createTree(arr,0,len(arr)-1)
