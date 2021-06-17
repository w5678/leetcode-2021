"""
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
思路：


"""
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        maps = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        lend = len(digits)
        out = []
        for i in range(lend):
            out = self.getmix(out, maps[digits[i]])
        return out

    def getmix(self, oldlist, newlist):
        retlist = set()
        if not oldlist: return newlist
        if not newlist: return oldlist
        for o in oldlist:
            for n in newlist:
                retlist.add(o + n)
        return list(retlist)


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        maps={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        ans=[""]
        for num in digits:
            ans=[per+suf for per in ans for suf in maps[num]]
        return ans
