/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    if(head==NULL)
        return NULL;
    if(head->next==NULL)
        return head;
    struct ListNode* t,*n;
    t=head->next;
    n = t->next;
    t->next = head;
    head->next = swapPairs(n);
    return t;
    
    
}
