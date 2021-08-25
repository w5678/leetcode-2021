"""
https://leetcode-cn.com/problems/minimum-size-subarray-sum/

给定一个含有 n 个正整数的数组和一个正整数 target 。


时间复杂度：$O(n)$
空间复杂度：$O(1)$

滑动窗口法做这个题目
因为是连续位置的数组元素，所以应该是一个队列
q=[]
q.insert(0,val)
q.pop()

在while True 死循环里面，判断q里的元素和是不是大于等于target是则pop出元素，如果不满足，则insert下一个数据。
最后求到q的长度的最小的那个值

比较满意，是自己很快做出来的


"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        q=[]
        #a.insert(0,val)
        #a.pop()
        minl=0
        if not nums:
            return 0
        i=0
        n=len(nums)
        while True:
            if sum(q)>= target:
                minl =min(len(q),minl) if minl else len(q)
                q.pop()
            elif i == n:
                break
            else:
                q.insert(0,nums[i])
                i+=1
        return minl


