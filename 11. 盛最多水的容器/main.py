"""
https://leetcode-cn.com/problems/container-with-most-water/

思路：
左右移动得到最大的容积
 左边小，就左边右移
 右边小，就右边左移
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        heightlen = len(height)
        bl, br = 0, heightlen - 1
        maxsum = 0
        while bl < br:
            if height[bl] < height[br]:
                b = height[bl]
                bl += 1
            else:
                b = height[br]
                br -= 1
            tmp = (br - bl + 1) * b
            if tmp > maxsum:
                maxsum = tmp
        return maxsum
