"""
计算字符串编辑距离: 可用于检查拼写，或者计算两句子之间的相似度（效果未知）
    最少需要多少个步骤能把wrong_str变成right_str
该算法具体原理还未清楚
"""

import numpy as np


def get_edit_distance(wrong_str, right_str):
    """
    计算距离
    :param wrong_str:
    :param right_str:
    :return:
    """
    m = len(wrong_str)
    n = len(right_str)
    d = np.zeros((m + 1, n + 1))
    # 初始化第一行和第一列
    for j in range(n + 1):
        d[0][j] = j
    for i in range(m + 1):
        d[i][0] = i
    for i in range(1, m + 1):
        ci = wrong_str[i - 1]
        for j in range(1, n + 1):
            cj = right_str[j - 1]
            if ci == cj:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i - 1][j - 1] + 1, min(d[i][j - 1] + 1, d[i - 1][j] + 1))
    return d[m][n]


if __name__ == '__main__':
    wrong_str = 'ha321ck'
    right_str = 'hsssssankcs'
    edit_distance = get_edit_distance(wrong_str, right_str)
    print(edit_distance)
