"""
https://leetcode-cn.com/problems/binary-search/


思路就是，二分逼近法
注意区间的问题 前闭后开，还是前闭后闭


"""



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            i = int((l+r+1)/2)
            if nums[i]== target:
                return i
            else:
                if nums[i] >target:
                    r= i-1
                else:
                    l=i+1
        return -1