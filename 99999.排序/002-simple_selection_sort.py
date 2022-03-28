# 简单选择排序
import random
from timeit import default_timer as timer
num_range=1000

def generate_nums(test_num_size):
    return [random.randint(0,num_range) for i in range(test_num_size)]



def simple_selection():
    num_size=100
    num_list = generate_nums(num_size)
    start=timer()
