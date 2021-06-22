"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/submissions/

没啥说的，这么做最简单
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        while len(nums) > len(set(nums)):
            for i in nums:
                if nums.count(i)>1:
                    nums.remove(i)
        return len(nums)