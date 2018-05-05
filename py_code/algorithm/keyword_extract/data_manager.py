"""
数据管理，目前用于读取数据
"""
import os


def get_text_content():
    dir_name, filename = os.path.split(os.path.abspath(__file__))
    text_dir = os.path.join(dir_name, 'data')
    text_path = os.path.join(text_dir, 'news_content.csv')
    file = open(text_path, mode='r', encoding='utf8')
    lines = file.readlines()
    file.close()
    return lines


if __name__ == '__main__':
    get_text_content()
