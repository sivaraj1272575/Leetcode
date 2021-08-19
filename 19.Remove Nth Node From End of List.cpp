/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count = 0;
        ListNode *newhead = new ListNode(0, head);
        ListNode *c = head, *p = newhead;
        while(c != NULL){
            count += 1;
            c = c->next;
        }
        
        int temp = count - n;
        
        for(int i=0; i<temp; i++)
            p = p->next;
        
        p->next = p->next->next;
        
        return newhead->next;
    }
};
