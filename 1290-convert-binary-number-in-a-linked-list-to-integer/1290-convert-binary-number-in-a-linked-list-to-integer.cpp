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
    int getDecimalValue(ListNode* head) {
        int i  = 0;
        ListNode *p = head;
        while(p != nullptr){
            i+= p->val;
            p=p->next;
            if(p != nullptr) i=i*2;
        } 
        return i;
    }
};