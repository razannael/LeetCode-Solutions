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
    public int pairSum(ListNode head) {
        if (head == null ) return 0;
        ListNode fast = head;
        ListNode slow = head;
        while (fast.next != null && fast.next.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode secondHalf = slow.next;
        slow.next = null;
        ListNode reversedSecondHalf = reverse(secondHalf);
        ListNode firstHalf = head;
        int maxTwinSum = firstHalf.val + reversedSecondHalf.val;
        while(head != null && reversedSecondHalf != null){
            maxTwinSum = Math.max(maxTwinSum , (firstHalf.val + reversedSecondHalf.val));
            firstHalf = firstHalf.next;
            reversedSecondHalf = reversedSecondHalf.next;
        }
        return maxTwinSum;
    }
        private ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
}