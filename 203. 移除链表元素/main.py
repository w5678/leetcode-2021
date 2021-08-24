"""

https://leetcode-cn.com/problems/remove-linked-list-elements/

给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

思路1：
虚拟节点，通过虚拟头部节点，可以完全放在while循环中做，而减少了一些边界的判断
public ListNode removeElements(ListNode head, int val) {
        ListNode header = new ListNode(-1);
        header.next = head;
        ListNode cur = header;
        while(cur.next != null){
            if(cur.next.val == val ){
                cur.next = cur.next.next;
            }else{
                cur = cur.next;
            }
        }
        return header.next;
    }
思路：此题删除链表中元素是很简单的，只需要让待删节点之前一个节点指向待删节点之后一个节点即可。 此题最大的问题就是，题目要求我们要返回新链表中的头结点，如果我们就采用仅仅复制头结点的方式(用H=head)然后用H进行操作，最后返回head。这样就会导致如果头结点也是我们需要删除的节点就会导致错误。当然我们可以采用循环操作判断第一个不是我们要删除的节点，但是这样有些麻烦。最好的方式就是我们创建一个新节点来作为整个链表的头结点，该节点中的值没有意义，只是用该节点来方便我们的操作。如果用H->next=head; 此时 我们操作H的话就把原先的头结点当做了一个普通节点来操作，此时原先的头结点就可以被删除了。最后返回H->next就满足条件了。正是由于有个无意义节点作为头结点会统一操作（把头结点当做普通节点）所以实际链表设计过程中都是有个无意义头结点的，遇到头结点不好解决的问题，大家可以设一个节点试试。


思路2：
链表和递归，联系很紧密
递归，反着来看，就是上一次返回的head，是我们这次的next

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        head.next = self.removeElements(head.next,val)
        return head.next if head.val ==val else head

