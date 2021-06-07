"""
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。


"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        mnlens = len(nums1) + len(nums2)
        if mnlens == 0: return 0
        if mnlens % 2 == 0:
            a, b = int((mnlens - 1) / 2), int((mnlens + 1) / 2)
        else:
            a, b = int((mnlens - 1) / 2), int((mnlens - 1) / 2)
        idx = 0
        sum = 0
        addcnt = 0
        s1, s2 = 0, 0
        maxnum = 10 ** 6
        while idx <= max(a, b):

            tmp1 = nums1[0] if nums1 else maxnum + 1
            tmp2 = nums2[0] if nums2 else maxnum + 1

            if tmp1 <= tmp2 and tmp1 <= maxnum:
                tmp = tmp1
                nums1.pop(0)
            elif tmp1 > tmp2 and tmp2 <= maxnum:
                tmp = tmp2
                nums2.pop(0)
            if idx in (a, b):
                sum += tmp
                addcnt += 1
            idx += 1
        return float(sum / addcnt)




