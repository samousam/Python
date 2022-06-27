##https://blog.csdn.net/weixin_41571493/article/details/81875088
# # 排序算法
# # 1. 交换排序
# # 1.1 冒泡排序(Bubble Sort)
#
# def BubbleSort(lst):
#     n=len(lst)
#     if n<=1:
#         return lst
#     for i in range (0,n):
#         for j in range(0,n-i-1):
#             if lst[j]>lst[j+1]:
#                 (lst[j],lst[j+1])=(lst[j+1],lst[j])
#     return lst
#
# print ("<<<Bubble Sort>>>")
# x=input("请输入待排序数列：\n")
# y=x.split()
# arr=[]
# for i in  y:
#     arr.append(int(i))
# arr=BubbleSort(arr)
# #print(arr)
# print("数列按序排列如下：")
# for i in arr:
#     print(i, end=' ')


# # 1.2 快速排序(Quick Sort)
# def QuickSort(lst):
#     # 此函数完成分区操作
#     def partition(arr, left, right):
#         key = left  # 划分参考数索引,默认为第一个数为基准数，可优化
#         while left < right:
#             # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
#             while left < right and arr[right] >= arr[key]:
#                 right -= 1
#             # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
#             while left < right and arr[left] <= arr[key]:
#                 left += 1
#             # 此时已找到一个比基准大的数，和一个比基准小的数，将他们互换位置
#             (arr[left], arr[right]) = (arr[right], arr[left])
#
#         # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
#         (arr[left], arr[key]) = (arr[key], arr[left])
#         # 返回目前基准所在位置的索引
#         return left
#
#     def quicksort(arr, left, right):
#         if left >= right:
#             return
#         # 从基准开始分区
#         mid = partition(arr, left, right)
#         # 递归调用
#         # print(arr)
#         quicksort(arr, left, mid - 1)
#         quicksort(arr, mid + 1, right)
#
#     # 主函数
#     n = len(lst)
#     if n <= 1:
#         return lst
#     quicksort(lst, 0, n - 1)
#     return lst
#
#
# print("<<< Quick Sort >>>")
# x = input("请输入待排序数列：\n")
# y = x.split()
# arr = []
# for i in y:
#     arr.append(int(i))
# arr = QuickSort(arr)
# # print(arr)
# print("数列按序排列如下：")
# for i in arr:
#     print(i, end=' ')


# # 2. 插入排序
# # 2.1 简单插入排序(Insert Sort)
#
# def InsertSort(lst):
#     n = len(lst)
#     if n <= 1:
#         return lst
#     for i in range(1, n):
#         j = i
#         target = lst[i]  # 每次循环的一个待插入的数
#         while j > 0 and target < lst[j - 1]:  # 比较、后移，给target腾位置
#             lst[j] = lst[j - 1]
#             j = j - 1
#         lst[j] = target  # 把target插到空位
#     return lst
#
# print("<<< Insert Sort >>>")
# x = input("请输入待排序数列：\n")
# y = x.split()
# arr = []
# for i in y:
#     arr.append(int(i))
# arr = InsertSort(arr)
# # print(arr)
# print("数列按序排列如下：")
# for i in arr:
#     print(i, end=' ')

# 2.2 希尔排序(Shell Sort)
def ShellSort(lst):
    def shellinsert(arr, d):
        n = len(arr)
        for i in range(d, n):
            j = i - d
            temp = arr[i]  # 记录要出入的数
            while (j >= 0 and arr[j] > temp):  # 从后向前，找打比其小的数的位置
                arr[j + d] = arr[j]  # 向后挪动
                j -= d
            if j != i - d:
                arr[j + d] = temp

    n = len(lst)
    if n <= 1:
        return lst
    d = n // 2
    while d >= 1:
        shellinsert(lst, d)
        d = d // 2
    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = ShellSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
