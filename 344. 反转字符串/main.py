"""
https://leetcode-cn.com/problems/reverse-string/

第一种循环法：
很简单，控制住终止条件就好了，两两交换


第二种，迭代：
构造迭代的条件
参数。
返回。
终止if ，start >= end
迭代拆解（逻辑，就是交换，进行下一对的迭代交换）

"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 循环法
        # if len(s)<2:
        #     return s
        # n=len(s)
        # for i in range(n):
        #     if (2*i) >= n:
        #         break
        #     s[i],s[n-i-1] = s[n-i-1],s[i]
        if not s:
            return ""
        self.s1(s ,0 ,len(s ) -1)

    def s1(self ,s ,start ,end):
        if start >= end:
            return
        self.s1(s ,start +1 ,end -1)
        s[start] ,s[end] = s[end] ,s[start]
