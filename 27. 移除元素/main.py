"""
https://leetcode-cn.com/problems/remove-element/

"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while nums.count(val)>0:
            nums.remove(val)
        return len(nums)
