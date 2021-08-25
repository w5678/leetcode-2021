"""
https://leetcode-cn.com/problems/next-greater-element-i/

给你两个 没有重复元素 的数组nums1 和nums2，其中nums1是nums2的子集。

请你找出 nums1中每个元素在nums2中的下一个比其大的值。
nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret=[]
        for n in nums1:
            idx= nums2.index(n)
            if idx==len(nums2)-1:
                ret.append(-1)
            else:
                while idx<len(nums2)-1:
                    idx+=1
                    if nums2[idx]>n:
                        ret.append(nums2[idx])
                        break
                    else:
                        pass
                else:
                    ret.append(-1)
        return ret
