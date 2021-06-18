"""
https://leetcode-cn.com/problems/merge-k-sorted-lists/submissions/

没想明白，还是看了大佬的答案
思路：
1，使用 heapq 来着当前最小的那个val的node
2，使用monkey patching 来给Node加入排序功能 ，实在是高
3，先将每个node 加入heap
4，pop出最小的那个node，随即在把这个node的next加入到heapq中
5，直到所有的都遍历结束

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        def __lt__(self,other):
            return self.val < other.val
        ListNode.__lt__ = __lt__
        import heapq
        heap=[]
        First = ListNode(0)
        p= First
        for l in lists:
            if l:
                heapq.heappush(heap,l)
        while heap:
            node = heapq.heappop(heap)
            p.next = ListNode(node.val)
            p=p.next
            if node.next:
                heapq.heappush(heap, node.next)
        return First.next
