/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // First, find the size of the linked list
        int listSize = 0;
        ListNode curr = head;
        while (curr != null) {
            curr = curr.next;
            ++listSize;
        }

        // If we need to remove the first node (head of the list)
        if (n == listSize) {
            return head.next;
        }

        curr = head;
        // Move to the node just before the one we want to remove
        for (int i = 1; i < listSize - n; i++) {
            curr = curr.next;
        }

        // Remove the nth node from the end
        curr.next = curr.next.next;
        return head;
    }
}
