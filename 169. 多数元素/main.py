"""
https://leetcode-cn.com/problems/majority-element/
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

1思路：
使用的是摩尔投票法
宏观来讲，和上一个相同则加一，不同则减一，如果有一个值数量过半，最坏的cnt也是1， res 也是该值
太溜了

2分治法：
将长的数组划分成小的数组，在每个小的数组上找出它的最多数
一层层递归
底层只有单个元素，它就是最多数
底2层只有2个元素，左右的最多数，一致的话就选它，不一致的话就找一个左右的最多数哪个多，选多的那个
依次类推

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res,cnt =0,0
        # for i in nums:
        #     if cnt == 0:
        #         res = i
        #         cnt+=1
        #     else:
        #         if i == res:
        #             cnt+=1
        #         else:
        #             cnt-=1
        # return res
        return self.getmajor(nums, 0, len(nums) - 1)

    def getmajor(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = l + (r - l) // 1
        leftm = self.getmajor(nums, l, mid)
        rightm = self.getmajor(nums, mid + 1, r)
        if leftm == rightm:
            return leftm
        leftc = 0
        rightc = 0
        for i in range(l, r + 1):
            if nums[i] == leftm:
                leftc += 1
            if nums[r] == rightm:
                rightc += 1
        return rightm if rightc > leftc else leftm