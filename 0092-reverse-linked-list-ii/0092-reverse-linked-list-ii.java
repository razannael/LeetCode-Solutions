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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0); // helper node
        dummy.next = head;
        ListNode prevReversing = dummy; // this node will refere to the node before the reversing prosess
        ListNode curr = head;
        for(int i =0; i <left-1; i++){ // iterate until reach the begining of the part will be reversed
            prevReversing = prevReversing.next;
            curr = curr.next;
        }
       ListNode subHead = curr; // the head of the part will be reversed
       ListNode prev = null ;
        for(int i = 0 ; i <= right - left; i++){ // the reversing prosess 
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        // in the next two lines we join the reversed sublist with other pieces
        prevReversing.next = prev;  
        subHead.next = curr;
        return dummy.next;
    }
}