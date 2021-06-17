"""
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/submissions/

思路：
找到那个要移除的元素位置
重新输出一个head
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_data=[]
        while head:
            node_data.append(head.val)
            head=head.next
        print(node_data)
        offset = len(node_data)-n
        print(offset)
        node_data = node_data[:offset]+node_data[offset+1:]
        print(node_data)
        h= None
        for d in node_data[::-1]:
            print(d)
            h1 = ListNode(d,next=h)
            h=h1
        return h

if __name__ == '__main__':
    sol =Solution()
    nums=[2,2,2,2]
    target=8
    print(sol.fourSum(nums,target))