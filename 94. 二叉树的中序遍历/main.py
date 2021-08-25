"""
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

给定一个二叉树的根节点 root ，返回它的 中序 遍历。

循环思路1：
利用stack的特性，先找到最左的一条线，然后从左下的叶子开始pop，依次循环每个node，
如果此时node有右孩子则append右孩子，这个右孩子是新加的，还要找它的左孩子，加入stack，以此类推，直到全部遍历完tree
就这样一边append 一边pop


递归思路2：
强大的递归，内在有许多的递归栈，实现了思路1的操作


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        if not root:
            return []
        stack = []
        cur = root
        res = []
        while stack or cur is not None:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res

