
import random
from timeit import default_timer as timer


def generate_nums(test_num_size):
    return [random.randint(0,num_range) for i in range(test_num_size)]


def insertsort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while (j>=0 and key< nums[j]):
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums

def main():
    list_size=40
    test_nums=generate_nums(list_size)
    print(test_nums)
    start= timer()
    test_nums = insertsort(test_nums)
    print("cost={}".format(timer()-start))
    print(test_nums)
    return test_nums

if __name__ == '__main__':
    main()