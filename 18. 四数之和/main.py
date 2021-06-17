"""
https://leetcode-cn.com/problems/4sum/submissions/

思路：
最后两个数，使用双指针来逼近
排序后的数组是一定的， 可以顺便去重
"""

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if not nums:
            return []
        nums.sort()
        lens=len(nums)
        data=[]
        for i in range(lens-3):
            for j in range(i+1,lens-2):
                l = j+1
                r= lens-1
                while l<r:
                    left = nums[l]
                    right =nums[r]
                    if nums[i]+nums[j]+left+right > target:
                        r-=1
                        while l<r and right == nums[r]:
                            r-=1
                    elif nums[i]+nums[j]+left+right < target:
                        l+=1
                        while l<r and left == nums[l]:
                            l+=1
                    else:
                        tmp=[nums[i],nums[j],left,right]
                        if  tmp not in data:
                            data.append(tmp)
                        l+=1
                        r-=1
                        while l<r and left == nums[l]:
                            l+=1
                        while l<r and right == nums[r]:
                            r-=1
        return data

if __name__ == '__main__':
    sol =Solution()
    nums=[2,2,2,2]
    target=8
    print(sol.fourSum(nums,target))
