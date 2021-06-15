"""
https://leetcode-cn.com/problems/longest-common-prefix/
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

思路：
1， 不可能大于最小的那个字符串
2，排除空字符串，返回空字符串
3，假定第一个字符串，每个位的字符进行比较

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        slen=len(strs)
        maxcnt = min(map(lambda x:len(x),strs))
        if maxcnt == 0:
            return ""
        target=strs[0][:maxcnt]
        for cnt in range(maxcnt):
            for i in range(slen):
                if target[cnt] != strs[i][cnt]:
                    if cnt==0:
                        return ""
                    else:
                        return target[:cnt]
        return target


