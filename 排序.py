# # https://developer.51cto.com/article/623936.html
# # 1.冒泡排序：逐步遍历列表比较相邻元素对，如元素的顺序错误，则交换元素；重复对列表中未排序部分的遍历，知道对列表进行排序
# arr = [26,27,2,4,19,36,48,50]
# #定义函数
# def bubble_sort(arr):
#     def swap(i,j):                          #交换函数def swap（x,y）:
#         arr[i],arr[j] = arr[j], arr[i]      #x,y = y,x
#     n = len(arr)
#     swapped = True
#     x = -1
#     while swapped:
#         swapped = False
#         x = x + 1
#         for i in range (1, n-x):
#             if arr[i-1] > arr[i]:
#                 swap(i-1,i)
#                 swapped = True
#     return arr
# #调用函数
# print(bubble_sort(arr))

# # 2.选择排序 默认“右选择排序”，优于冒泡，在未排序的子列表找到最小元素，并将其放已排序子列表末尾，不断获取最小末排序元素，重复进行，直到列表完全排序
# arr = [3, 44, 38, 5, 47, 15, 36, 26, 46, 4, 19, 50, 48]
# def selection_sort(arr):
#     for i in range(len(arr)):
#         minimum = i
#         for j in range(i+1,len(arr)):   # 选择最小值
#             if arr[j] < arr[minimum]:
#                 minimum = j
#         arr[minimum], arr[i] = arr[i], arr[minimum] #把它放在已排序的数组结尾
#     return arr
#
# #调用函数
# print(selection_sort(arr))

# # 3.插入排序，快，简单，从数组中删除一个元素，在另一个派苏数组中查找该元素所属位置，将其插入，重复过程，直到没有输入元素保留
# arr = [9, 8, 5, 7, 1, 3, 6, 4, 2]
# def insertion_sort(arr):
#     for i in range(len(arr)):
#         cursor = arr[i]                         # 光标，游标
#         pos = i                                 # 位置
#         while pos > 0 and arr[pos - 1] > cursor:
#             arr[pos] = arr[pos - 1]             # 交换列表中的数字
#             pos = pos - 1
#         arr[pos] = cursor                       # 中断并进行最终交换
#     return arr
#
# #调用函数
# print(insertion_sort(arr))

# # 4. 合并排序
# # （1）连续分割未排序的列表，有N个子列表，每个列表有1个未排序，N是数组元素数
# # （2）反复合并，将两个子列表合并一起，生成新的已排序列表，直到所有元素合并到一个已排序的数组
# arr = [5, 6, 3, 1, 8, 7, 2, 4]
# def merge_sort(arr):
#     if len(arr) <= 1:  # 对最后一个数组进行拆分
#         return arr
#     mid = len(arr) // 2  # 商 整数部分 #在两个部分上递归执行merge_sort
#     left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
#     return merge(left, right, arr.copy())  # 合并在一起
#
# def merge(left, right, merged):
#     left_cursor, right_cursor = 0, 0
#     while left_cursor < len(left) and right_cursor < len(right):
#         if left[left_cursor] <= right[right_cursor]:  # 将每一个排序并放入结果
#             merged[left_cursor + right_cursor] = left[left_cursor]
#             left_cursor += 1
#         else:
#             merged[left_cursor + right_cursor] = right[right_cursor]
#             right_cursor += 1
#     for left_cursor in range(left_cursor, len(left)):
#         merged[left_cursor + right_cursor] = left[left_cursor]
#     for right_cursor in range(right_cursor, len(right)):
#         merged[left_cursor + right_cursor] = right[right_cursor]
#     return merged
#
# # 调用函数
# print(merge_sort(arr))

# 5. 快速排序（分割）
# (1) 从数组中选择一个元素，为轴pivot
# (2) 将小于轴的元素移到轴左侧，大于轴的元素移到右侧，为分区操作
# (3) 递归地将上诉2步骤分别应用于元素的每个子数组，这些元素的值比一个州的值小或大

arr = [5, 6, 3, 1, 8, 7, 2, 4]
def partition(arr, begin, end):
    pivot_id = begin
    for i in range(begin+1, end+1):
        if arr[i] <= arr[begin]:
            pivot_id += 1
            arr[i], arr[pivot_id] = arr[pivot_id], arr[i]
    arr[pivot_id],arr[begin] = arr[begin], arr[pivot_id]
    return pivot_id
def quick_sort_recursion(arr,begin,end):
    if begin >= end:
        return
    pivot_id  = partition(arr, begin, end)
    quick_sort_recursion(arr, begin, pivot_id - 1)
    quick_sort_recursion(arr,pivot_id + 1, end)
def quick_sort(arr,begin=0,end=None):
    if end is None:
        end = len(arr) - 1
        return quick_sort_recursion(arr, begin, end)

print(quick_sort_recursion(arr, begin=0, end=None))






