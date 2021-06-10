"""
https://leetcode-cn.com/problems/string-to-integer-atoi/submissions/

思路：
去除空格，判断第一个字符 + 还是-
然后判断是不是数字
其实简单的，关键是我审题不清楚
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        flag=1
        s= s.lstrip()
        if not s:
            return 0
        import re
        if s[0] in ("+","-"):
            flag={"+":1,"-":-1}[s[0]]
            s=s[1:]
        idx,start,end=0,None,None
        int_nums=["0","1","2","3","4","5","6","7","8","9"]
        while idx<len(s):
            if s[idx] in int_nums:
                if start is None:
                    start=idx
                    end=idx
                else:
                    end=idx
            else:
                break
            idx+=1
        if start is None:
            return 0
        nums=s[start:end+1]
        num =int(nums) *flag
        minv = -1 * (2**31)
        maxv = (2**31)-1
        if num < minv:
            return minv
        if num > maxv:
            return maxv
        return num

if __name__ == '__main__':
    sol =Solution()
    s="21474836460"
    print(sol.myAtoi(s))