# _*_ coding=utf-8 _*_


import numpy as np

"""花式索引"""
"""
问题1：给一个数组，选出数组中位置为1,3,4,6,7个元素，组成新的数组
"""
arr = np.arange(10)
print(arr[[1, 3, 4, 6, 7]])

"""
问题2：给一个二维数组，选出数组中第一列和第三列，组成新的二维数组
"""
arr2 = np.arange(10).reshape(2, 5)
print(arr2)
print(arr2[:, [1, 3]])  # :取到所有的行，[1,3]取到第一列和第三列


