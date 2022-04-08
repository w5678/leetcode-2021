import random
from timeit import default_timer as timer

class MySort():

    def __init__(self):
        self.num_range = 1000
        self.list_size = 50000

    def generate_nums(self):
        return [random.randint(0, self.num_range) for i in range(self.list_size)]

    def dubble_sort(self,show=0):
        test_nums =self.generate_nums()
        if show:print(test_nums)
        start = timer()
        for i in range(self.list_size-1):
            flag=0
            for j in range(self.list_size-i-1):
                if test_nums[i] > test_nums[j]:
                    test_nums[j], test_nums[i] = test_nums[i], test_nums[j]
                    flag=1
            if flag==0: break
        print("dubble_sort: cost = {}s".format(timer() - start))
        if show: print(test_nums)
        return test_nums

    def insert_sort(self,show=0):
        test_nums =self.generate_nums()
        if show: print(test_nums)
        start = timer()
        for i in range(1, self.list_size):
            key = test_nums[i]
            j = i - 1
            while (j >= 0 and key < test_nums[j]):
                test_nums[j + 1] = test_nums[j]
                j -= 1
            test_nums[j + 1] = key
        print("insert_sort: cost = {}s".format(timer() - start))
        if show: print(test_nums)
        return test_nums

    def select_sort(self,show=0):
        """类似于人工选择
        在一堆里面找到最小的，放在0位置
        然后依次寻找，直到len-1位置为止
        """
        test_nums =self.generate_nums()
        if show: print(test_nums)
        start = timer()
        for i in range(0, self.list_size-1):
            j=i+1
            index=j
            while j<self.list_size:
                if test_nums[j] < test_nums[index]:
                    index =j
                j+=1
            test_nums[i],test_nums[index] = test_nums[index],test_nums[i]
        print("select_sort :cost = {}s".format(timer() - start))
        if show: print(test_nums)
        return test_nums

    def insert_half_sort(self,show=0):
        """能够节省一些比较的时间，整体提升不大"""
        test_nums =self.generate_nums()
        if show: print(test_nums)
        start = timer()
        for i in range(1,self.list_size):#i从第1个开始
            key = test_nums[i] #第i个值记录下来
            l, r = 0, i-1 #限定二分法搜索的边界
            while l<=r: #结束条件，相等
                mid = l+(r-l)//2 #防止溢出
                if key >=test_nums[mid]:
                    l=mid+1 #l移动+1 位置
                elif key < test_nums[mid]:
                    r=mid-1 #r移动到-1位置
            #跳出while时，l是i的值要插入的位置
            j=i-1
            while j>=l:#区域值的移动 l 到 i-1之间的值都要左移，因为要空个位置l用于插入
                test_nums[j+1] = test_nums[j]
                j-=1
            test_nums[l]=key#移动结束把 原来i位置的值放进去
        print("insert_half_sort: cost = {}s".format(timer() - start))
        if show: print(test_nums)
        return test_nums

    def shell_sort(self,show=0):
        """思路就是大网筛完小网筛
        集合中基本有序，减少了移动次数
        """
        test_nums =self.generate_nums()
        if show:print(test_nums)
        start = timer()
        offset= self.list_size//2#初始的offset 为长度的一半
        while offset >0:#当offset为0时候退出while
            for i in range(offset, self.list_size): #从offset到size范围内筛，网眼大小为offset
                key = test_nums[i] #保持值
                j = i#界定范围 offset开始到 i为止
                while (j >= offset and key < test_nums[j-offset]):#这里检查下一个offset的值，为了方便移动
                    test_nums[j] = test_nums[j-offset] # 这是一个向右移动的过程
                    j -= offset #插入的移动距离是一个网眼 offset
                #while 退出时候，满足了j位置值 从小于key 到大于等于key的节点，放在这
                test_nums[j] = key
            offset= offset//2# offset减半
        print("shell_ sort: cost = {}s".format(timer() - start))
        if show:print(test_nums)
        return test_nums

    def quick_sort(self,show=0):
        """递归是最快的虽然不稳定
        NlogN 常数项最小
        """
        test_nums =self.generate_nums()
        if show:print(test_nums)
        start = timer()
        self._quick_sort(test_nums,0,self.list_size-1)#这里的low 和high是元素的起始索引和终点索引
        print("shell_ sort: cost = {}s".format(timer() - start))
        if show: print(test_nums)
        return test_nums

    def _quick_sort(self,nums,left,right):#递归参数
        if left>=right: #递归终点
            return
        i,j =left,right #将left，right
        key =nums[i] #假设为选取范围内的0号位置的值为中间值
        while i <j: #控制左右不越界
            while (i <j and key <= nums[j]): #从右边一直向左找，直到找到第一个小于key的值，j
                j-=1
            nums[i] = nums[j]# 比key小的值拿来放在 左边 寻找位置上
            while (i <j and key >= nums[i]):#从左边一直向右找，直到找到第一个大于key的值，i
                i+=1
            nums[j]=nums[i]#比key大的值拿来放在 右边 寻找位置上
        #while退出时，左右两边都找完了，保证了i 左边的都是小于key的区域，i右边的都是大于key的区域
        nums[i]=key #此时i的位置就是key值 真实的位置，不再动了，
        # 接下来i位置划分的两个区域 （小于key的区域，大于key的区域）分别进行这种操作，递归
        self._quick_sort(nums,left,i-1)
        self._quick_sort(nums, i+1, right)



if __name__ == '__main__':
    ms= MySort()
    # ms.insert_half_sort()
    # ms.select_sort()
    ms.dubble_sort()
    # ms.insert_sort()
    ms.shell_sort()
    ms.quick_sort()
