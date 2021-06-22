"""
https://leetcode-cn.com/problems/swap-nodes-in-pairs/
思路：
递归的方法来做
使用递归只需要考虑当前与下一次递归的关系，并且要限定边界
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next =head
        return next
