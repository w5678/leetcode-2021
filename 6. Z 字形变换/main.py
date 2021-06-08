"""
https://leetcode-cn.com/problems/zigzag-conversion/

目的就是将数据 有目的的划分

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        if len(s)<=numRows:
            return s
        lines=[]
        s0=list(s[0:numRows])
        s=list(s)
        s=s[numRows:]
        #累加尖头
        flag=True
        while flag:
            _start=numRows-2
            _end=numRows+numRows-3
            step=2*numRows-2
            if len(s)<step:
                flag=False
                missed_steps=step-len(s)
                for i in range(missed_steps):
                    s.append("")
            tmp = []
            for i in range(_start,_start+numRows,1):
                if i == _start:
                    tmp.append(s[i])
                elif i==_end:
                    tmp.append(s[i])
                else:
                    _=i-_start
                    tmp.append(s[_start-_]+s[i])
            lines.append(tmp)
            s=s[step:]
        res=s0
        for i in range(numRows):
            for line in lines:
                res[i]+=line[i]
        outstr=""
        for s in res:outstr+=s
        print(outstr)
        return outstr















if __name__ == '__main__':
    s="PAYPALISHIRING"
    sol =Solution()
    sol.convert(s,3)
