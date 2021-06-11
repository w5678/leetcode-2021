class Solution:
    def romanToInt(self, s: str) -> int:
        d={
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
        }
        d1={
            "IV":1,
            "IX":1,
            "XL":10,
            "XC":10,
            "CD":100,
            "CM":100,
        }
        sums = sum([d[k] for k in s])
        idx=0
        while idx<len(s)-1:
            sums-=d1.get(s[idx:idx+2],0)*2
            idx+=1
        return sums


if __name__ == '__main__':
    sol=Solution()
    s="MCMXCIV"
    print(sol.romanToInt(s))