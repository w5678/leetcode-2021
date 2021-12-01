"""
删除单链表中的倒数第n个node
"""
from LinkNode import  Node
from LinkNode import create_linklist,show_linklist



class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        nodes=[]
        cur =head
        while cur:
            nodes.append(cur)
            cur = cur.next
        if n == len(nodes): #需要判断是不是头节点
            return head.next
        cnt=1
        while nodes:
            x= nodes.pop()
            if cnt == n+1:
                x.next=x.next.next # 这个条件不适用于头节点
            cnt+=1
        return head



def test_case1():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = create_linklist(nums)
    show_linklist(head)
    s = Solution()
    head1 = s.removeNthFromEnd(head, 9)
    show_linklist(head1)


def test_case2():
    nums = [1]
    head = create_linklist(nums)
    show_linklist(head)
    s = Solution()
    head1 = s.removeNthFromEnd(head, 1)
    show_linklist(head1)





if __name__ == '__main__':
    test_case1()
