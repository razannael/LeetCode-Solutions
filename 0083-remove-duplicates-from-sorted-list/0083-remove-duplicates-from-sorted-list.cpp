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
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head || !head->next) return head;
        int curr_val = head->val;
        ListNode* prev_head = head;
        ListNode* temp_head = head->next;
        while(temp_head){
           if(curr_val != temp_head->val){
            curr_val = temp_head->val;
            prev_head = temp_head;
            temp_head = prev_head->next;
           }else{
            prev_head->next = temp_head->next;
            temp_head = prev_head->next;
           }
        }
        return head;
    }
};