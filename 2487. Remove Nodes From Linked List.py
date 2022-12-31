# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head != None:
            while len(stack)>0 and head.val > stack[-1].val:
                stack.pop()
            stack.append(head)
            head = head.next
        
        if len(stack) == 0:
            return None
        temp = stack[0]
        for i in range(1, len(stack)):
            temp.next = stack[i]
            temp = temp.next
        temp.next = None
        return stack[0]
        
