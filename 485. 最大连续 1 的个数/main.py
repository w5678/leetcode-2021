"""

https://leetcode-cn.com/problems/max-consecutive-ones/


执行用时：
3748 ms
, 在所有 Python3 提交中击败了
5.32%
的用户
内存消耗：
19.2 MB
, 在所有 Python3 提交中击败了
5.04%
的用户


"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=0
        while nums.pop(0):
            n+=1
            if not nums:
                return n
        return max(n,self.findMaxConsecutiveOnes(nums))
