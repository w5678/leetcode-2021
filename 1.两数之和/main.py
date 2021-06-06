"""
https://leetcode-cn.com/problems/two-sum/

执行用时：
4292 ms,在所有 Python3 提交中击败了5.01%的用户
内存消耗：
14.9 MB, 在所有 Python3 提交中击败了48.21%的用户
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []








