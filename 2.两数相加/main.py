"""
https://leetcode-cn.com/problems/add-two-numbers/
执行用时：
68 ms
, 在所有 Python3 提交中击败了
67.13%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
35.83%
的用户


"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=""
        s2=""
        while l1:
            s1+="{}".format(l1.val)
            l1=l1.next
        while l2:
            s2+="{}".format(l2.val)
            l2=l2.next
        s3=str(int(s1[::-1])+int(s2[::-1]))
        l3=None
        for k in s3:
            next=l3
            l3=ListNode(val=int(k),next=next)
        return l3


