"""
https://leetcode-cn.com/problems/divide-two-integers/
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

思路：
1， 使用递归的方式来做
2， 每次递归，先进行边界值检查，再减掉差值
3， 递归的核心，就是将除数向左位移，当达到大于被除数时候得到i，此时的i-1为当前的倍数，减掉后仍有余量，进入下次递归时候被除数是这次的余量，进行累加
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        i, a, b = 0, abs(dividend), abs(divisor)
        if a == 0 or a < b:
            return 0
        while b <= a:
            b = b << 1
            i = i + 1
        else:
            res = (1 << (i - 1)) + self.divide(a - (b >> 1), abs(divisor))
            if (dividend ^ divisor) < 0:
                res = -res
            return min(res, (1 << 31) - 1)

