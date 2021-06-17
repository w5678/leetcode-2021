"""
https://leetcode-cn.com/problems/generate-parentheses/

思路：
找到规律，就是在每个位置上放置()
可以使用递归来做
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n ==1:
            return ["()"]
        elif n ==2 :
            return ["()()","(())"]
        else:
            return list(set([x[0:i]+"()"+x[i:] for x in self.generateParenthesis(n-1) for i in range(2*n-2)]))
