"""
目前暂时不实现分词。使用jieba代理分词。
"""
import os

import jieba


def get_combine_stop_words():
    """
    获得combine_stop_word.txt中的所有停用次
    :return:
    """
    dir_name, filename = os.path.split(os.path.abspath(__file__))
    par_name = os.path.dirname(dir_name)
    par_name = os.path.dirname(par_name)
    par_name = os.path.dirname(par_name)
    dic_path = os.path.join(par_name, 'dictionary')
    dic_path = os.path.join(dic_path, 'stopword')
    dic_path = os.path.join(dic_path, 'combine_stop_word.txt')
    file = open(dic_path, mode='r', encoding='utf8')
    lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.replace('\n', '')
    file.close()
    return lines


stop_words = get_combine_stop_words()


def segment_word_and_delete_stop_word(content):
    """
    输出一篇文本内容，进行分词的同时剔除停用词
    :param content:
    :return:
    """
    seg_words = jieba.cut(content)
    return_list = []
    for word in seg_words:
        if word not in stop_words:
            return_list.append(word)
    return return_list


if __name__ == '__main__':
    text = '原标题：朗恩儿童美语完成千万级天使轮融资，基于线下学校打造幼教行业社区芥末堆3月8日讯，近日，儿童英语培训品牌“朗恩儿童美语”获得千万级天使轮融资，投资方为安芙兰资本。朗恩儿童美语创立于江苏省苏州市，向3至12' \
           '岁儿童提供线下的英语培训课程及教学服务，目前已进入10多座城市，截至2017年6月，共有43家分校、1200多名教师、13000' \
           '多名学员。江苏桀笙教育培训有限公司总裁、朗恩教育共享社区创始人王俊卿表示，过去几年公司的重点是朗恩儿童美语' \
           '的直营校扩张和加盟校管理，公司将在标准化、精细化运营校区的同时，以朗恩儿童美语的直营校和加盟校为基础，建立“' \
           '朗恩教育共享社区”。朗恩教育共享社区的定位是幼教行业资源整合平台，提供的服务包括教育创业人才孵化、一线招生经纪人' \
           '才孵化、教育场地共享、教育质量评估与监控、教育投资渠道对接等服务。融资确定后，朗恩儿童美语将加快“新一线、强二' \
           '线”城市的布局，完成20个重点城市的网点建设，依托旗下线下直营校区和加盟校区，把线下运营逐步互联网化，打造共享社区，' \
           '计划2年建设100家教育社区。返回搜狐，查看更多责任编辑： '
    segment_word_and_delete_stop_word(text)
    # get_combine_stop_words()
