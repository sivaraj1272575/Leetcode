class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergelists(lst1,lst2):
            if lst1 == None:
                return lst2
            elif lst2 == None:
                return lst1
            else:
                result = None
                if lst1.val<lst2.val:
                    result = lst1
                    result.next = mergelists(lst1.next,lst2)
                else:
                    result = lst2
                    result.next = mergelists(lst1,lst2.next)
                return result
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            last = len(lists)-1
            while last!=0:
                i = 0
                j = last
                while i<j:
                    lists[i] = mergelists(lists[i],lists[j])
                    i+=1
                    j-=1
                    if j<=i:
                        last = j
            return lists[0]
