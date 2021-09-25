"""
https://leetcode-cn.com/problems/count-number-of-homogenous-substrings/

给你一个字符串 s ，返回 s 中 同构子字符串 的数目。由于答案可能很大，只需返回对 109 + 7 取余 后的结果。

同构字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同构字符串。

子字符串 是字符串中的一个连续字符序列。

思路：
1，遍历所有的字符，保存上一个字符为last，与当前字符比较，如果相同则 inc++，否则inc=1 重新开始
2，cnt每次叠加inc
3，最后的返回值 取余数 %
"""

class Solution:
    def countHomogenous(self, s: str) -> int:
        if not s:
            return 0
        i,cnt=0,0
        last=s[0]
        inc=0
        while i <len(s):
            if last == s[i]:
                inc+=1
            else:
                inc=1
            last = s[i]
            i+=1
            cnt+=inc
        return cnt % (10**9+7)

if __name__ == '__main__':
    s=Solution()
    print(s.countHomogenous("vvvvvvllll"))