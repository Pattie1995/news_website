# -*- coding:utf-8 -*-
import jieba
if __name__ == '__main__':
    file_name = "test.txt"
    content = open(file_name, "rb").read()
    # print(content)
    seg_list = jieba.cut(content, cut_all=False)  # 精确模式
    print("精确模式:" + "/".join(seg_list))
    # data = open("新建文本文档.txt").readlines()
    # seg_list = jieba.cut("我来到北京清华大学", cut_all=True) #全模式
    # print("全模式:" + "/".join(seg_list))



    # seg_list = jieba.cut("他来到了网易杭研大厦", HMM=False) #不使用HMM模型
    # print("不使用HMM模型： "+"/".join(seg_list))
    #
    # seg_list = jieba.cut("他来到了网易杭研大厦", HMM=True) #使用HMM模型
    # print('使用HMM模型：'+"/".join(seg_list))
    #
    # seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", HMM=False) #搜索引擎模式
    # print("搜索引擎模式："+"/".join(seg_list))
    #
    # seg_list = jieba.lcut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", HMM=True)
    # print(seg_list)
