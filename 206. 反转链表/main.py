"""
https://leetcode-cn.com/problems/reverse-linked-list/


给你单链表的头节点 head ，请你反转链表，并返回反转后的链表

思路：
使用双指针法
1，第一个指针用于从前往后，弹出元素
2，第二个指针，把pre当成next，给他按上 第一个指针pop出的head
3，返回pre

中间注意要保存一下，next的对象，因为反转后，next会变掉
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 双指针解法
        # pre=None #原始的node，原始值为None
        # cur=head #是一个遍历的指针
        # while cur:
        #     temp=cur.next #先保存下遍历指针next的节点，就可以拿出来cur了
        #     cur.next =pre #当前的pre比较 head，把cur单独拿出来，next上绑上pre，就实现了相邻二者的反转
        #     pre=cur# 再把这个反转后的 cur，当成pre，准备给下次的当狗
        #     cur=temp #保存好的next，可以用了
        # return pre #最后返回 pre

        #迭代解法
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next= head
        head.next=None
        return p
