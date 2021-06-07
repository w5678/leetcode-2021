"""
https://leetcode-cn.com/problems/longest-palindromic-substring/
给你一个字符串 s，找到 s 中最长的回文子串。
总结：
类似于递归的方式，将所有位置间隔字符串是否为回文，全部写在dp里
往后延伸时候会调用较小的间隔
太难了

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen=len(s)
        dp=[[False]*slen for _ in range(slen)]
        for j in range(0,slen):
            for i in range(j,-1,-1):
                dp[i][j]=(s[i]==s[j]) and(i+1>j-1 or dp[i+1][j-1] )
        start,maxlen=0,0
        for i in range(slen):
            for j in range(i,slen):
                if dp[i][j] and (j-i+1>maxlen):
                    start=i
                    maxlen=j-i+1
        return s[start:start+maxlen]

