"""
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

思路1：循环
先拿到到最左边，再开始pop，然后判断当前节点，是否有右孩子，或者该右孩子保存过了
如果满足条件，则开add值，并且prev =cur
不满足条件，再次将cur入站，cur=cur.right。并且找它的最左的节点，
依次类推
关键的关键就是判断，是否能确认是不是能获取它的值，得保证它没有右孩子，或者右孩子已经添加了


思路2 ：递归
和思录


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
        stack=[]
        res=[]
        cur=root
        prev=None
        while stack or cur:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur= stack.pop()
                if not cur.right or cur.right is prev:
                    res.append(cur.val)
                    prev = cur
                    cur=None
                else:
                    stack.append(cur)
                    cur=cur.right
        return res