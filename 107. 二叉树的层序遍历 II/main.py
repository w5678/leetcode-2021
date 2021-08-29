"""
https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/

给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）


思路和102 题一样，将绕在里面的关系铺成一层一层的，
根据res的插入方式来达到这种目的


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        empty=[]
        full=[root]
        res=[]
        while full or empty:
            d=[]
            while full:
                node = full.pop()
                d.append(node.val)
                if node.left:
                    empty.insert(0,node.left)
                if node.right:
                    empty.insert(0,node.right)
            res.insert(0,d)
            empty,full = full,empty
        return res
