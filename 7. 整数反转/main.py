class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        n = int(x[::-1] if not x.startswith("-") else -int(x[1:][::-1]))
        return 0 if n < -2 ** 31 or n > 2 ** 31 - 1 else n


if __name__ == '__main__':
    sol=Solution()
    sol.reverse(1534236469)

