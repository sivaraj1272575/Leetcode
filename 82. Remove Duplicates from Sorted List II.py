class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *newNode = new ListNode(0, head);
        ListNode *prev = newNode, *cur = head;
        while(cur != NULL){
            int flag = 0;
            while(cur->next != NULL && cur->val == cur->next->val){
                cur = cur->next;
                flag = 1;
            }
            if(flag == 1){
                prev->next = cur->next;
                cur = cur->next;
            }else{
                prev = prev->next;
                cur = cur->next;
            }
        }
        return newNode->next;
    }
};
