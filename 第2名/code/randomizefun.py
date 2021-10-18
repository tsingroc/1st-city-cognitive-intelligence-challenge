import os


def randomizefun(prag, mod):  # 从样本列表中进行随机抽样
    f = open('access.txt', 'r')  # 打开限行规则库
    ac = f.readlines()  # 将文件按行读取成list
    Acc1 = open("access1.txt", "w+")  # 打开写入目标文件
    for i in range(1, len(ac)):  # 逐行进行判断
        for j in prag:  # 枚举每一个取模余数
            if i % mod == j:  # 同余则抽样
                Acc1.write(ac[i])  # 将抽样结果写入输出
                break  # 找到一个同余项则退出
    Acc1.close()  # 关闭写入目标文件

# 寻找最优结果


# for mod0 in range(20, 30):  # 枚举基本抽样间隔
#     for i in range(1, 5):  # 枚举抽样间隔得倍数
#         mod = mod0 * i  # 获取本次得实际抽样间隔
#         for a1 in range(0, mod):  # 枚举第一个抽样位置
#             for a2 in range(a1, mod):  # 枚举第二个抽样位置
#                 for a3 in range(a2, mod):  # 枚举第三个抽样位置
#                     for a4 in range(a3, mod):  # 枚举第四个抽样位置
#                         for a5 in range(a4, mod):  # 枚举第五个抽样位置
#                             for a6 in range(a5, mod):  # 枚举第六个抽样位置
#                                 randomizefun([a1, a2, a3, a4, a5, a6], mod)  # 执行抽样
#                                 os.system('pause')  # 停止程序，运行仿真评估限行结果


# 复现提交结果仅需按照如下代码逐行取消注释并执行即可，每次解除一行的注释


randomizefun([1, 5, 10, 17, 22], 24)  # 第一次迭代抽样
# randomizefun([2, 3, 11, 20, 26, 27], 48)  # 第二次迭代抽样
# randomizefun([2, 3, 12, 20, 38, 39], 48)  # 第三次迭代抽样
# randomizefun([2, 7, 13, 19, 25, 37], 48)  # 第四次迭代抽样
