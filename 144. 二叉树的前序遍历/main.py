"""
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

给你二叉树的根节点 root ，返回它节点值的 前序 遍历。


1思路：
使用循环的方式来做，结合着stack来做，近似将一个node拿掉之后，剩下的是两个node，再按照先左后有的方式求值，
按照前序遍历的方式，需要先获取左子树的值，再右子数的值，所以每次先append right ，再append left，在大while循环中，
不停的重复这个动作，直到所有的节点都结束


2思路：
很巧妙的使用 递归，实现了思路1的效果



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # stack=[root]
        # res=[]
        # while stack:
        #     node =stack.pop()
        #     res.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return res
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)