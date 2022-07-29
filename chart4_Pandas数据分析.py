# -*- coding:utf-8 -*-
# @Time : 2022/7/28 11:14 上午
# @Author : Bin Bin Xue
# @File : chart4_Pandas数据分析
# @Project : python_data_analysis

'''
    4.1 Pandas数据结构及其创建
        1_Pandas数据结构概述
            Series和DataFrame

    4.2 DataFrame基本操作
        1_基本列操作
            增加、修改
                df['列标'] = ['value1',..]
            检索
                df['列标']
            删除
                del df['列标']
                df.pop('列标') - 返回删除的列
                df.drop('列标',axis=1)' - 返回删除后的剩余值

        2_基本行操作
            检索
                df.loc['行标'] - 按照自定义的索引
                df.iloc['行标'] - 按照原来的索引
            增加
                df.loc['行标'] = ['v1'...] - 列表添加行
                df.loc['行标'] = {'key1':'value1',...} - 字典添加行
            修改
                df.loc['行标'] = {..} - 同上
            删除
                df.drop(['行标1','行标2'..],inplace=True) - inplace表示修改原值

    4.3 Pandas检索
        1_基本检索
            检查前5行
                df.head()
            检查后5行
                df.tail()
            检查行索引
                df.index
            检索列索引
                df.columns

        2_多行检索
            索引号索引（左闭又开）
                df[0:10] - 返回前10行
                df.iloc[0:10] - 同上
            索引标签索引（双闭）
                df.loc[0:10] - 返回标签为0-10的行

        3_多列检索
            df[['列标1','列标2'...]]

        4_行列检索
            df[0:10][['列标1']] - 返回1列，10行
            df.loc[0:10,['列标1','列标2']] - 按自定义的索引号索引
            df.iloc[0:10,:4] - 按原始序号索引
            reindex进行检索：
            (1)按行：
                df.reindex([行号1,行号2])
            (2)按列：
                df.reindex(columns=['列标1','列标2'])
            (3)行列：
                df.reindex(index=[行号1,行号2],columns=['列标1','列标2','列标3'])

        5_条件检索
            df[df['列标']=='列值'] - 这是一个条件，可加符号连接多个条件：==、!=、&、｜、-
                举例：
                    df2 = df.loc[0:200,['name','score','amount']]
                    df2[(df2['score']>4.5)&(df2['amount']>500)]

        6_重新检索
            reindex(['索引1','索引2'..])
                行索引重新排序（如果reindex中的索引存在与原来的不同的则直接添加新索引，赋值为None）
            reindex(range(6),method='ffill')
                用前向填充方法填充缺失值

        7_更换检索
            更换索引值
                df.set_index('列标') - 列标所在列成为索引值
            重置索引值
                df.reset_index(drop=True) - 重置索引值为顺序序列（drop=True表示去掉原索引值）

    4.4 Pandas数据运算
        1_算数运算
            df1.add(df2,fill_value=0) - 相当于df1+df2，并用0填充缺失值
            df1.sub(df2) - 减
            df1.mul(df2) - 乘
            df1.div(df2) - 除

        2_排序
            按索引排序
                df.sort_index(ascending=False) -按降序排序
            按值排序
                df.sort_values(axis,ascending=False)

        3_函数应用和映射
            使用自定义的方法处理数据：
                (1)df.apply(方法名,axis=1)
                    函数调用到Dataframe的一行/列上
                (2)df.map(方法名)
                    函数调用到Series的每一个元素上
                (3)df.applymap(方法名)
                    函数用到DataFrame的每一个元素上

        4_统计方法
            df.describe() - 描述统计
            频数统计：
                obj = pd.Series(...)
                obj.unique()
                obj.value_counts()

    4.5 Pandas处理缺失值
        1_查找缺失值
            df.isnull()
            df.notnull()
            df.info()
        2_删除缺失值
            df.dropna(axis=0,how='any',thresh=None,subset=None,inplace=False)
        3_填充缺失值
            df.fillna(value,method,axis,inplace)
                整体填充（用0或均值填充缺失值）
                    df.fillna(0,inplace=True)
                    df.fillna(df1.mean(),inplace=True)
                字典填充（分列填充）
                    df.fillna({1:0.88,2:0.66})
                        表示第2列缺失值用0.88填充，第3列用0.66
                前向填充
                    df.fillna(method='ffill')

    4.6 数据载入与输出
        1_读/写文本文件
            读取文件：
                pd.read_csv(.csv文件)
                pd.read_table(.csv文件,sep=',')
            写入文件：
                pd.to_csv()
        2_读/写Excel文件
            读取文件：
                pd.read_excel(xls或xlsx文件路径,'Sheet1')
                pd.to_excel()

    4.7 数据聚合与分组
        1_merge数据合并（要求有相同的列名作为连接键）
            pd.merge(df_left,df_right,left_on='a1',right_on='b1',how='inner').fillna('unknows')
                默认为内连接，不填充空值
                可设置为左外连接、右外连接、外连接；指定用于合并的连接键；设置空值填充值

        2_concat轴向连接（不需要有连接键，直接堆叠）
            pd.concat([s1,s2,s3..])
        3_检测与处理重复值
            判断重复数据：
                df.duplicated()
            去重：
                整体去重：
                    df.drop_duplicates()
                按列去重：
                    df.drop_duplicates(['列名1','列名2'])
                去重时保留的是最后的记录
                    df.drop_duplicates(keep='last')
        4_数据分组
            分组：
                grb = df.groupby('列名').groups
            查看分组：
                grb.get_group('列包含的类型值')
            链式操作（左到右做运算）：
                zoo.groupby('animal').sum().drop(columns='uniq_id').sort_values('water_need',ascending=False)
                （分组->求和->删除一列->按列降序排列）
'''