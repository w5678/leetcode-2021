"""
https://leetcode-cn.com/problems/search-insert-position/

二分法最重要的概念， 区间

while的退出条件，关系着l 和 r数据的区间 关系，
比如 初始化r= n-1的时候，l==r 允许存在 [l,r]，则区间内找不到时候，l>r ,则此时返回r+1

比如 初始化r= n的时候，l==r 不允许存在 [l,r)，则区间内找不到时候，l>r ,则此时返回r


"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            i = l + int((r - l) / 2)
            if nums[i] == target:
                return i
            else:
                if nums[i] > target:
                    r = i - 1
                else:
                    l = i + 1
        return r + 1


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        l, r = 0, n
        while l < r:
            i = l + int((r - l) / 2)
            if nums[i] == target:
                return i
            else:
                if nums[i] > target:
                    r = i
                else:
                    l = i + 1
        return r
