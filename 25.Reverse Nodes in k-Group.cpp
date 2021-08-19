class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head == NULL)
            return NULL;
        ListNode *cur = head;
        for(int i=1; i<k; i++){
            cur = cur->next;
            if(cur == NULL)
                return head;
        }
        
        ListNode *prev = NULL, *nxt;
        cur = head;
        for(int i=0; i<k ; i++){
            nxt = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nxt;
        }
        head->next = reverseKGroup(cur, k);
        return prev;
    }
};
