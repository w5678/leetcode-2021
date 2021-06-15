"""
https://leetcode-cn.com/problems/3sum-closest/

思路：
1，最接近意味着距离的绝对值最小
2，先从小到大排序，再遍历i，从i+1作为左指针，nlen-1 作为右指针，进行双指针操作
3，当前和比target小 left 右移变大
    当前和比target大 right 左移变小
"""

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        nlen=len(nums)
        val=nums[0]+nums[1]+nums[2]
        diff=abs(val-target)
        for i in range(nlen-2):
            l=i+1
            r=nlen-1
            val0= nums[i]+nums[l]+nums[r]
            diff0= abs(val0-target)
            while l<r:
                val1 = nums[i]+nums[l]+nums[r]
                diff1=abs(val1-target)
                if diff1 < diff0:
                    diff0 =diff1
                    val0 = val1
                if val1 == target:
                    return val1
                elif val1 > target:
                    r-=1
                else:
                    l+=1
            if diff0 < diff:
                diff = diff0
                val = val0
        return val


