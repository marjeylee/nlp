"""
根据语料库建立模型
"""
import json
import os
from collections import defaultdict
from math import log

from py_code.algorithm.keyword_extract.data_manager import get_text_content
from py_code.algorithm.word_segment.word_segment_proxy import segment_word_and_delete_stop_word
from py_code.utility.file_operate import delete_files

dir_name, filename = os.path.split(os.path.abspath(__file__))
model_path = os.path.join(dir_name, 'model')


class ModelBuilder:
    def __init__(self):
        self.idf_dic = None
        pass

    @staticmethod
    def remove_previous_model():
        """
        删除以前建立的模型，
        删除model文件夹下的所有文件
        :return:
        """
        delete_files(model_path)

    def create_new_model(self):
        """
        重新初始化一个模型
        :return:
        """
        self.remove_previous_model()
        self.idf_dic = defaultdict(int)

    def add_content(self, content):
        """
        :param content: 文章内容
        :return:
        """
        words = segment_word_and_delete_stop_word(content)
        words = set(words)  # 过滤相同的
        words = list(words)
        for word in words:
            self.idf_dic[word] = self.idf_dic[word] + 1

    @staticmethod
    def save_model(json_content):
        """
        保存模型
        :param json_content:
        :return:
        """
        file_path = os.path.join(model_path, 'idf.model')
        with open(file_path, mode='w', encoding='utf8') as file:
            file.write(json_content)


def get_idf_dict(total_text, count_dic):
    """
    获取idf——dic
    :param total_text:
    :param count_dic:
    :return:
    """
    i_dict = defaultdict()
    for key in count_dic.keys():
        alp = float(total_text) / (float(count_dic[key] + 1.0))
        value = log(alp)
        i_dict[key] = value
    return i_dict


if __name__ == '__main__':
    builder = ModelBuilder()
    builder.create_new_model()
    contents = get_text_content()
    for text_content in contents:
        builder.add_content(text_content)
    total_content = 1320
    idf_dict = get_idf_dict(total_content, builder.idf_dic)
    json_str = json.dumps(idf_dict)
    builder.save_model(json_str)
    print(1)
