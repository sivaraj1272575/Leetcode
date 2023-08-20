# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if a == b:
                return a
            if a > b:
                return gcd(a-b, b)
            else:
                return gcd(a, b-a)
        
        prev, cur = None,  head

        while cur.next != None:
            next = cur.next
            new_node = ListNode(val = gcd(cur.val, next.val))
            cur.next = new_node
            new_node.next = next
            cur = next
        
        return head
