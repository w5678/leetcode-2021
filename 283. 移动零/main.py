"""
https://leetcode-cn.com/problems/move-zeroes/

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

1 思路：
采用了双指针法
快指针用来遍历 nums的每一个元素
慢指针来保存新的顺序，非0的存入其中
最后在利用慢指针来补0
较为优

2思路：
利用python的remove的特性
先remove再最后追加
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        l = len(nums)
        j = 0
        for i in range(l):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < l:
            nums[j] = 0
            j += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if len(nums) <2:
        #     return
        # l=len(nums)
        # j=0
        # for i in range(l):
        #     if nums[i]!=0:
        #         nums[j]=nums[i]
        #         j+=1
        # while j<l:
        #     nums[j]=0
        #     j+=1
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
