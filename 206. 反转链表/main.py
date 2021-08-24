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
        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next =pre
            pre=cur
            cur=temp
        return pre

