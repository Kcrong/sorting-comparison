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


# 삽입 정렬
@CalcTime
def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        key = num_list[i]
        j = i - 1
        while j >= 0 and key < num_list[j]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
            j -= 1
        num_list[j + 1] = key


# 버블 정렬
@CalcTime
def bubble_sort(num_list):
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - i):
            if num_list[j - 1] > num_list[j]:
                num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]


if __name__ == '__main__':
    print("Selection Sort: ")
    after_sort = selection_sort(nums)

    print("Insertion Sort: ")
    after_sort = insertion_sort(nums)

    print("Bubble Sort: ")
    after_sort = bubble_sort(nums)