import random
from timeit import default_timer as timer
num_range=10

def generate_nums(test_num_size):
    return [random.randint(0,num_range) for i in range(test_num_size)]

def dubble_sort(test_nums):
    """两两交换
    从i=0 位置开始往后面i+1位置开始遍历，找到比他小的就交换，直到结束
    """
    # list_size=10000
    # test_nums=generate_nums(list_size)
    list_size=len(test_nums)
    start= timer()
    for i in range(0,list_size):
        for j in range(i+1,list_size):
            if test_nums[i] > test_nums[j]:
                test_nums[j],test_nums[i]= test_nums[i],test_nums[j]
    print("cost={}".format(timer()-start))
    print(test_nums)
    return test_nums

def binary_search(nums,k):
    if not nums:
        return 0
    start,end =0, len(nums)-1
    while start <= end:
        mid = start+(end-start)//2
        if k==  nums[mid]:
            return mid
        elif nums[mid] >k:
            end=mid-1
        else:
            start = mid + 1
    return start



    

if __name__ == '__main__':
    numlist= generate_nums(20)
    numlist = dubble_sort(numlist)
    print(numlist)
    idx= binary_search(numlist,6)
    print("6 ->",idx)
    