"""
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/


我自己完全第一遍就做出来的，
人的潜力真是无穷的

使用两个队列来做这些事情，
空闲队列和正用队列
正用队列pop出来的左右孩子塞到 空闲队列中，正用队列pop完了后，空闲队列和正用队列 交换下

退出循环的条件是：
都pop完了，即树都遍历完了  

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        empty=[]
        using=[root]
        res=[]
        while empty or using:
            using_pops=[]
            while using:
                cur = self.pop_q(using)
                using_pops.append(cur.val)
                if cur.left:
                    self.push_q(empty,cur.left)
                if cur.right:
                    self.push_q(empty,cur.right)
            empty,using = using,empty
            res.append(using_pops)
        return res

    def push_q(self,q,val):
        q.insert(0,val)

    def pop_q(self,q):
       return q.pop()