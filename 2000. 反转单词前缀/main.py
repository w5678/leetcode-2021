"""
https://leetcode-cn.com/problems/reverse-prefix-of-word/

思路：就是操作字符串，两步搞定


"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        return word if idx== -1 else word[0:idx+1][::-1]+ word[idx+1:]