# -*- coding:utf-8 -*-
# @Time : 2022/7/28 10:22 上午
# @Author : Bin Bin Xue
# @File : chart2_python程序设计基础
# @Project : python_data_analysis

'''
    2.1 python语言基础
        （1）print(value,sep=' ',end='\n')
                    sep为多个值输出后之间的间隔符；
                    end为输出语句末尾自动添加的字符（设为空值就能保证不换行）
        （2）组合数据类型自带的方法：
                    列表：（增、删、查、排序、频数）
                                list.index(x) - 查找与x相同的第一个元素索引
                                list.count(x) - 统计x出现的次数
                                list.append(x) - 将x元素追加到列表末尾
                                list.extend(t) - 将序列t添加到表尾
                                list.insert(i,x) - 元素x插入到列表list中索引为i的位置
                                list.remove(x) - 删除列表中第一个与x相同的元素
                                list.pop([i]) - 删除列表中索引为i的元素
                                list.clear() - 清空列表
                                list.reverse() - 翻转列表
                                list.sort() - 对列表元素排序(默认升序）
                    元组：（查、频数）
                                tuple.index(x)
                                tuple.count(x)
                    字符串:（填充、大小写互换、类型检测、子串操作、划分、连接、替换、去除特定字符）
                                str.center(w,filchar) - 在字符串两边填充w个filchar
                                str.rjust(w,filchar) - 字符串在右，左边填充w个filchar
                                str.ljust(w,filchar)
                                str.lower() - 变小写
                                str.upper() - 变大写
                                str.capitalize() - 首字母大写，其他小写
                                str.title() - 字符中每个单词首字母大写，其他小写
                                str.swapcase() - 字符大小写互换
                                str.islower() - 判断是否全为小写
                                str.isupper() - 判断是否全为大写
                                str.isdigit() - 判断字符串是否为数字
                                str.find(sub_str) - 查找子串sub_str
                                str.index(sub_str) - 同上，找不到会返回异常
                                str.count(sub_str) - 统计子串频次
                                str.split(sep) - 按sep划分字符串
                                str.join(iterable) - 连接字符串
                                str.replace(old,new) - 替换字符串
                                str.strip(charts) - 去除两侧的空白符或指定字符
                                字符串格式化：
                                    str.format(i,k,n) - i,k,n依次填充str中的'{}'
                    字典：（查、删、增、更、取）
                                dict.clear() - 移除字典中的元素
                                dict.get(key) - 返回key对应的value值
                                dict.pop(k) - 移除key
                                dict.popitem() - 移除末尾一个键值对
                                dict.setdefault(key) - 插入值为default的键key
                                dict.update([]) - 使用键值对更新原有的
                                dict.items() - 返回一个键-值对视图
                                dict.keys() - 返回一个键视图
                                dict.values() - 返回一个值视图

'''
# 使用str.format输出99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j,i,j*i),end=' ')
    print()