"""
https://leetcode-cn.com/contest/weekly-contest-260/problems/maximum-difference-between-increasing-elements/


思路：
暴力求解法，获取后面元素与之前面元素的最大的差值
"""

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        maxdiff = -1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxdiff = max(maxdiff, nums[i] - nums[j])
        return maxdiff

