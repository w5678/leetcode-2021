"""
https://leetcode-cn.com/problems/linked-list-cycle/

使用快慢指针来解决边界问题

注意要next问None的情况

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        f=head
        s=head
        while head.next and s.next and f.next and f.next.next:
            s=s.next
            f=f.next.next
            if s == f:
                return True
        return False

