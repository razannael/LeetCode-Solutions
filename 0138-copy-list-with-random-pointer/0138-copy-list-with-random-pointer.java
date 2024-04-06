/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head==null) return null;
        Node cop=head;
        while(head!=null){
            Node n=new Node(head.val);
            n.next=head.next;
            head.next=n;
            head=head.next.next;
        }
        head=cop;
        
        while(head!=null){
            head.next.random=(head.random!=null)?head.random.next:null;
            head=head.next.next;
        }
        head=cop;
        Node head2=head.next;
        Node cop2=head2;
        while(head!=null&&head2!=null&&head.next!=null&&head2.next!=null){
            head.next=head.next.next;
            head2.next=head2.next.next;
            head=head.next;
            head2=head2.next;
        }
    head.next=null;
        return cop2;

    }
}