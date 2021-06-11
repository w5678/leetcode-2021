class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            return False
        pidx=0
        ps=[]
        while pidx < len(p):
            thisc = p[pidx]
            prevc = None if pidx ==0 else p[pidx-1]
            if thisc == "*":
                ps[-1]=[prevc,20]
            elif thisc == '.':
                ps.append(['_',1])
            else:
                ps.append([thisc, 1])
            pidx += 1
        print(ps)
        slen =len(s)
        s1=list(filter(lambda x:x[1]==1,ps))
        s2=list(filter(lambda x:x[1]!=1,ps))
        print("s1={}".format(s1))
        print("s2={}".format(s2))
        maxloop = slen -len(s1)
        print(maxloop)





if __name__ == '__main__':
    sol =Solution()
    s="aabcddfff"
    p="c*a*bcd.f*"
    sol.isMatch(s,p)
