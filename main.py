from time import time

with open('nums.txt', 'r') as f:
    raw_nums = f.readlines()

nums = [int(i.split('\n')[0]) for i in raw_nums]


class CalcTime:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        before = time()
        self.func(*args, **kwargs)
        print(time() - before)


# 선택 정렬
@CalcTime
def selection_sort(num_list):
    for i in range(len(num_list)):
        using_list = num_list[i:]
        min_idx = using_list.index(min(using_list)) + i
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

    return num_list


if __name__ == '__main__':
    print("Selection Sort: ")
    after_sort = selection_sort(nums)

