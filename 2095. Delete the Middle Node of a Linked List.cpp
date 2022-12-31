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
    ListNode* deleteMiddle(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return NULL;
        
        ListNode *slow=head, *fast=head;
        ListNode *odd = NULL;
        while(fast->next != NULL && fast->next->next !=NULL){
            if(fast->next->next != NULL && fast->next->next->next == NULL){
                odd = slow;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        if(fast->next == NULL){
            odd->next = odd->next->next;
        }else{
            slow->next = slow->next->next;
        }
        return head;
    }
};
