# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head==None or head.next == None:
            return head
        n = 0
        temp = head
        while temp!=None:
            n+=1
            temp = temp.next
        k = k%n
        if k == 0:
            return head
        temp = head
        for i in range(k+1):
            temp = temp.next
        temp1 = head
        while temp!=None:
            temp1 = temp1.next
            temp = temp.next
        x = temp1.next
        y = x
        temp1.next = None
        while x!=None and x.next!=None:
            x = x.next
        if x!=None:
            x.next = head
        return y
