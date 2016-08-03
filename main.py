from time import time

with open('nums.txt', 'r') as f:
    raw_nums = f.readlines()

nums = [int(i.split('\n')[0]) for i in raw_nums]


# 선택 정렬
def selection_sort(num_list):
    for i in range(len(num_list)):
        using_list = num_list[i:]
        min_idx = using_list.index(min(using_list)) + i
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

    return num_list


if __name__ == '__main__':
    print("Selection Sort: ")
    after_sort = selection_sort(nums)
