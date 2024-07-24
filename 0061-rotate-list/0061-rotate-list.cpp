class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || k == 0) return head;

        // First, find the length of the list and the last node
        ListNode* last = head;
        int length = 1;
        while (last->next) {
            last = last->next;
            length++;
        }

        // Connect the last node to the head to make it a circular list
        last->next = head;

        // Find the new tail position
        k = k % length; // To handle cases where k is greater than length
        int stepsToNewHead = length - k;

        ListNode* newTail = head;
        for (int i = 1; i < stepsToNewHead; i++) {
            newTail = newTail->next;
        }

        // Set the new head and break the circular link
        ListNode* newHead = newTail->next;
        newTail->next = nullptr;

        return newHead;
    }
};
