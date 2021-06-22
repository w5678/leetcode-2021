""":cvar
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/submissions/

思路：
还是使用递归来做，
1，另外封装函数输出当前的head 和 end
2，return head,
3，将end和下一次的递归联系起来

成果：
终于做了个难题了，
慢慢弄懂了一点递归的思想
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        vals=[]
        for i in range(k):
            if not head:
                h,end= self.reverseNode2(vals[::-1])
                return h
            vals.append(head.val)
            head=head.next
        else:
            h,end = self.reverseNode2(vals)
            end.next=self.reverseKGroup(head,k)
            return h



    def reverseNode2(self, vals):
        h = None
        end=h
        for v in vals:
            if not end:
                h = ListNode(v, h)
                end=h
            else:
                h = ListNode(v, h)
        return h,end



if __name__ == '__main__':
    sol =Solution()
    vals=[1,2,3,4,5,6,7,8,9,10,11]
    nodes = sol.reverseNode(vals)
    print(nodes)
    print(sol.printnodes(nodes))
    h1=sol.reverseKGroup(nodes,3)
    print("****")
    print(sol.printnodes(h1))




