# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : replace_filename.py


import os
if __name__ == '__main__':
    # 设定文件路径
    path='D:\\PycharmProjects\\pythonProject\\test_top10_hospital\\test_png'
    i=1
    # 对目录下的文件进行遍历
    for file in os.listdir(path):
        # 判断是否是文件
        if os.path.isfile(os.path.join(path,file))==True:
            # 设置新文件名
            name="test_"
            new_name=file.replace(name,"")
        # 重命名
        os.rename(os.path.join(path,file),os.path.join(path, new_name))
        i+=1


