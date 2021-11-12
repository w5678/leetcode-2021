"""
https://leetcode-cn.com/problems/maximum-subarray/

思路：
这个使用动态规划DP来做，关键是要找这次的结果和上次的结果有什么关系。
1，使用vs来保存每次的时候的最大值，vs[i] = max(vs[i-1]+nums[i],nums[i])
2， vs[i] =vs[i-1]+nums[i] 表示 nums[i]为正的
3， vs[i] =nums[i] 表示 vs[i-1] 是负的
4， 还需要一个result来记录过程中的值，因为不一定vs[i] 就一定大于vs[i-1],比如vs[i-1] =-10， nums[i] = -7


"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) <=1:
            return sum(nums)
        vs = [0]*len(nums)
        vs[0]= nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            vs[i] = max(vs[i-1]+nums[i],nums[i])
            result =max(result,vs[i] )
        return result


"""
另一种的dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <1:
            return 0
        for i in range(1, len(nums)):
            nums[i] = nums[i]+max(nums[i-1],0)
        return max(nums)

"""