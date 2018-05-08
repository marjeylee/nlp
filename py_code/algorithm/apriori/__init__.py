"""
Apriori算法，用于求置信度　support({A,B}) = num(A∩B) / W = P(A∩B)
为了降低所需的计算时间，研究人员发现一种所谓的Apriori原理。Apriori原理可以帮我们减少可能感兴趣的项集。
Apriori原理是说如果某个项集是频繁的，那么它的所有子集也是频繁的。上图给出的例子，这意味着如果{0,1}是频繁的，那么{0}、{1}也一定是频繁的。
这个原理直观上并没有什么帮助，但是如果反过来看就有用了，也就是说如果一个项集是非频繁集，那么它的所有超集也是非频繁的
"""
from collections import defaultdict


def get_total_set(data_list):
    """
    获取所有单项的set
    :return:
    """
    class_set = set()
    for group in data_list:
        for item in group:
            class_set.add(item)
    return class_set


def contain_all(parent, child):
    """
    看子集合中的所有元素是否都在父集合中
    :param parent:
    :param child:
    :return:
    """
    if (parent is None or len(parent) < 1) or (child is None or len(child) < 1):
        return False
    for ch in child:
        if ch not in parent:
            return False
    return True


def get_satisfy_num(val_items, data_list):
    """
    看满足条件的集合或者父集合的个数。
    :param val_items:
    :param data_list:
    :return:
    """
    satisfy_num = 0
    for data in data_list:
        if contain_all(data, val_items):
            satisfy_num = satisfy_num + 1
    return satisfy_num


def get_satisfy_dict(validate_set, data_list, support):
    """
     获取满足条件的合集以及频次
    :param validate_set:
    :param data_list:
    :return:
    """
    satisfy_list = []
    satisfy_num = len(data_list) * support
    for val_item in validate_set:
        num = get_satisfy_num(val_item, data_list)
        if satisfy_num <= num:
            li = [val_item, num]
            satisfy_list.append(li)
    return satisfy_list


def get_validate_set(total_satisfy_map, current_layer):
    """
    获取下一层待验证集
    :param total_satisfy_map:
    :param current_layer:
    :return:
    """
    last_list = total_satisfy_map[current_layer - 1]
    last_set = set()
    validate_set = []
    for l_list in last_list:
        for l in l_list[0]:
            last_set.add(l)
    last_set = list(last_set)
    size = len(last_set)
    for i in range(current_layer):
        pass


def apriori(data_list, support):
    """
    算法实现，
    :param
    data_list:
    :param
    support: 支持度
    :return:
    """
    class_set = get_total_set(data_list)  # 所有输入类型的dict
    total_satisfy_map = {}
    validate_set = []  # 待验证集合
    for class_type in class_set:
        validate_set.append([class_type])
    current_layer = 1
    while current_layer > 0:
        satisfy_dict = get_satisfy_dict(validate_set, data_list, support)
        if len(satisfy_dict) == 0:
            break
        total_satisfy_map[current_layer] = satisfy_dict
        current_layer = current_layer + 1
        validate_set = get_validate_set(total_satisfy_map, current_layer)


if __name__ == '__main__':
    egs = [[1, 2, 3, 4, 5, 7], [1, 4, 2, 3], [1, 2], [1, 3, 2, 4, 5, 6], [2, 3, 5, 1, 6], [12, 1, 2, 3], [12, 1, 2, 3],
           [12, 1, 2, 3], [12, 1, 2, 3], [12, 1, 3], [1, 2, 3], [12, 1, 2], [12, 1, 3], [1, 2, 5], [2, 4], [2, 3],
           [1, 2, 4], [1, 3], [2, 3], [1, 3], [1, 2, 3, 5], [1, 2, 3], [1, 2, 5], [2, 4], [2, 3], [1, 2, 4], [1, 3],
           [2, 3], [1, 3], [1, 2, 3, 5], [1, 2, 3], [1, 2, 5], [2, 4], [2, 3], [1, 2, 4], [1, 3], [2, 3], [1, 3],
           [1, 2, 3, 5], [1, 2, 8]]
    result = apriori(egs, 0.2)
