"""
https://leetcode-cn.com/problems/remove-element/


思路1：

思路2：
双慢指针来做
i 从0 个元素开始
j 从最后一个元素
终止条件是i >= j

i指针移动+1，不是val时候停下来，等待交换
j指针移动-1，是val时候停下来，等待交换
==> 这样做的话，将val都挤在头部


"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while nums.count(val)>0:
            nums.remove(val)
        return len(nums)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while nums.count(val)>0:
        #     nums.remove(val)
        # return len(nums)
        if len(nums)==0:
            return 0
        i,j = 0,len(nums)-1
        while i <j:# i==j ?
            while i<j and nums[i] !=val:
                i+=1
            while i<j and nums[j] ==val:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        return i if nums[j]==val else i+1 #i是序号