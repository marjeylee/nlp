"""
文件操作工具类
"""
import os


def delete_files(dir_path):
    """
    删除目录以及目录下的文件
    :param dir_path:
    :return:
    """
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            del_file = os.path.join(root, name)
            os.remove(del_file)
