"""
https://leetcode-cn.com/problems/implement-strstr/submissions/

思路：
很简单
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(haystack) < len(needle):
            return -1
        if haystack == needle:
            return 0
        for idx in range(len(haystack) - len(needle) + 1):
            if haystack[idx:idx + len(needle)] == needle:
                return idx
        return -1

