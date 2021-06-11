"""
https://leetcode-cn.com/problems/palindrome-number/submissions/
换种思路，将其转换为字符串，
使用递归的方式来做

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.check_str(str(x))

    def check_str(self, xs: str) -> bool:
        if xs[0] == "-":
            return False
        elif len(xs)==1:
            return True
        if xs[0] == xs[-1]:
            if len(xs) ==2:
                return True
            else:
                return self.check_str( xs[1:-1])
        else:
            return False

if __name__ == '__main__':
    sol =Solution()
    x=1000021
    print(sol.isPalindrome(x))
