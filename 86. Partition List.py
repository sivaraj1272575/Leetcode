# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        def getNode(n):
            newnode = ListNode()
            newnode.val = n
            newnode.next = None
            return newnode
        h1 = getNode(0)
        h2 = getNode(0)
        l1 = h1
        l2 = h2
        t = head
        while t!=None:
            if t.val < x:
                l1.next = getNode(t.val)
                l1 = l1.next
            else:
                l2.next = getNode(t.val)
                l2 = l2.next
            t = t.next
        l1.next = h2.next
        return h1.next
