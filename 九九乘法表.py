##方法一
# i = 1
# while i < 10:  # 控制行，1到9
#     j = 1
#     while j <= i:  # 控制每行显示的数量，1到9
#         print("%d*%d=%d" % (i, j, i * j), end=' ')  # 输出
#         j += 1  # 每行显示的数量加1
#     print()  # 每一行结束换行
#     i += 1  # 行数加1

##方法二 格式化输出 print("%d"%)
# for i in range (1,10):
#     print('\n')
#     for j in range (1, i+1):
#         print("%d*%d=%d"% (i, j, i*j), end=" ")

# #方法三 字符串格式化 print(f"{}")
# for i in range (1,10):
#     print('\n')
#     for j in range (1, i+1):
#         print(f"{i}*{j}={i*j}", end=" ")