"""
https://leetcode-cn.com/problems/pascals-triangle/

这个就是很纯粹的dp思路
1， 当前行的数据和上一行的数据相关，k[i] =k-1[i-1]+k-1[i]

"""



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            d= [1]*(i+1)
            if i >=2:
                for k in range(1,i):
                    d[k] = pre[k-1]+pre[k]
            result+=[d]
            pre =d
        return result
