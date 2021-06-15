"""
https://leetcode-cn.com/problems/3sum/submissions/

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

思路：
1，如果正常使用三次遍历循环必定超时
2，采用左右指针法来做，小了左移一位，大了右移一位
3，不能重复以为着，需要跳过重复的数字
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results=[]
        nums.sort()
        slen=len(nums)
        for i in range(slen):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            left =i+1
            right =slen-1
            while left < right:
                if nums[left]+ nums[right]< -nums[i]:
                    l=nums[left]
                    left+=1
                    while left<right and l == nums[left]:
                        left+=1
                elif nums[left]+ nums[right]> -nums[i]:
                    r=nums[right]
                    right-=1
                    while left<right and r == nums[right]:
                        right-=1
                else:
                    l=nums[left]
                    r=nums[right]
                    while left<right and r == nums[right]:
                        right-=1
                    while left<right and l == nums[left]:
                        left+=1
                    tmp=[nums[i],l,r]
                    results.append(tmp)
        return results


