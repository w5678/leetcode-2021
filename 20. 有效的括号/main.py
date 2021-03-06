"""
https://leetcode-cn.com/problems/valid-parentheses/submissions/

思路：
使用递归来做，就比如这样的连续判断类型的


"""
class Solution:
    def isValid(self, s: str) -> bool:
        lefts=["(","[","{"]
        rights=[")","]","}"]
        lens = len(s)
        cnt =lens-1
        rightp=None
        leftp=None
        rval = ""
        lval = ""
        while cnt>-1:
            if s[cnt] in rights:
                rval=s[cnt]
                lval = lefts[rights.index(s[cnt])]
                rightp =cnt
            elif s[cnt] in lefts:
                if lval == "":
                    return False
                if s[cnt] == lval:
                    leftp = cnt
                    s1 = s[:leftp]+s[leftp+1:rightp]+s[rightp+1:]
                    return self.isValid(s1)
                else:
                    return False
            cnt-=1
        if rightp is None and leftp is None:
            return True
        else:
            return False

    """
    使用stack来做，
        lefts=["(","[","{"]
        rights=[")","]","}"]
        lens = len(s)
        cnt =lens-1
        stack=[]
        for k in s:
            if k in lefts:
                stack.append(k)
            if k in rights:
                if not stack:
                    return False
                k1=stack.pop() 
                if rights.index(k) == lefts.index(k1):
                    pass
                else:
                    return False
        if len(stack):
            return False
        return True

    
    """





if __name__ == '__main__':
    sol  =Solution()
    s="s]"
    print(sol.isValid(s))




