"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/submissions/

思路：
先排序
在重新生成新的链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        data=[]
        while l2 or l1:
            if not l1 and l2:
                data.append(l2.val)
                l2= l2.next
            elif not l2 and l1:
                data.append(l1.val)
                l1= l1.next
            elif l1.val <= l2.val:
                data.append(l1.val)
                l1=l1.next
            else:
                data.append(l2.val)
                l2=l2.next
        print(data)
        head=None
        for v in data[::-1]:
            head = ListNode(v,head)
        return head

