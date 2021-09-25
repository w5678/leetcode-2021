"""
https://leetcode-cn.com/problems/minimum-changes-to-make-alternating-binary-string/

思路就是：
1，对于一个既定的字符串，从1 开始或从0 开始，操作的步骤是不一样的
2，需要分别去test 操作次数，并且取最小值

"""


class Solution:
    def minOperations(self, s: str) -> int:
        return min(self.startWith1(s),self.startWith0(s))

    def startWith1(self,s:str) -> int:
        i,cnt=0,0
        key=0
        maps={
            1:"1",
            0:"0"
        }
        while i<len(s):
            key = key^1
            if s[i] == maps[key]:
                pass
            else:
                cnt+=1
            i+=1
        return cnt

    def startWith0(self,s:str) -> int:
        i,cnt=0,0
        key=1
        maps={
            1:"1",
            0:"0"
        }
        while i<len(s):
            key = key^1
            if s[i] == maps[key]:
                pass
            else:
                cnt+=1
            i+=1
        return cnt
