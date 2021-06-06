"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/submissions/

思路：
（1）ans 就是最大的不重复间隔，要么就是两个相同的字符间隔的最大值，要么就是整个字符串的长度
 值是动态的，每次都会重新求值
（2）start 就是不重复字符串的起始位置
   当出现重复时候 start需要调整位置
（3）将出现过的值存起来，key是值，value是位置


太难了，我不会做，看了这个神仙解法，666

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res={}
        start,ans=0,0
        for j in range(len(s)):
            if s[j] in res:
                start=max(res[s[j]],start)
            ans=max(ans,j-start+1)
            res[s[j]]=j+1
        return ans

