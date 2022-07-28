# -*- coding:utf-8 -*-
# @Time : 2022/7/28 11:14 上午
# @Author : Bin Bin Xue
# @File : chart3_Numpy基础
# @Project : python_data_analysis

'''
    3.1 多维数组对象ndarray
        1_创建
            np.arrange(1,10)
            np.arrange(1.2,1.3,1.4)
                按指定序列
            np.linspace(1,12,5)
                按等差序列
            np.logspace(1,2,5)
                按等比序列
            np.zeros(3,4)
                创建3行4列全0矩阵
            np.zeros_like(a)
                创建和a同型全0矩阵
            np.ones(3,4)
                创建3行4列全1矩阵
            np.ones_like(a)
                创建和a同型全1矩阵
            np.eye(4)
                创建4维主对角线全1方阵
            np.eye(4,1)
                创建4维第二对角线全1方阵
            np.diag([1,2,3,4])
                按照序列值创建对角方阵
        2_属性
            np.T - 转置
            np.dtype - 元素类型
            np.shape - 数组形状
            np.ndim - 数组维度
            np.size - 元素个数
            np.itemsize - 每个元素的尺寸
        3_随机数组
            np.random.rand()
                生成[0,1]区间内，符合均匀分布的一个随机数
            np.random.randn(2,3)
                生成标准正态分布的随机数组，2行3列
            np.random.randint(1,100,(3,5))
                生成[1,100)区间内的随机数组，3行5列
            ..normal(loc,scale,size)
                生成均值为loc，标准差为scale的正态分布
            ..binomial
                生成二项分布
            ..poisson
                生成泊松分布
            ..uniform
                生成均匀分布
            ..shuffle(x)
                对x中的数据随机排序，改变原对象
            ..permutation(x)
                同上，不改变原对象，返回一个随机排序的新对象

    3.2 数组操作
        1_索引和切片
        2_形状变换
            数组重塑：.reshape(new_shape)，.resize(new_shape) - 前不变，后改变原数组
            数组展平：.ravel()，.flattern() - 前返回一个视图，后返回新副本，都不改变原数组
            数组转置：.transpose(0,1,2)，.swapaxes(0,1) - 前返回任意一个轴互换，后返回两个轴互换
            数组合并：.concatenate(k)，vstack()，hstack() - 值为0时纵向合并；为1时横向合并
            数组拆分：.split(k) - 划分成k个部分
    3.3 数组运算
            算数运算：  np.abs(a) - 计算数组中各元素的绝对值
                                sqrt(a) - 平方根
                                square(a) - 平方
                                log(a)/log2(a)/log10(a) - 对数
                                sign(a) - 取符号
                                ceil(a) - 向上取整
                                floor(a) - 向下取整
                                cos(a)/sin(a)/tan(a) - 三角函数
                                arcos(a)/arcsin(a)/arctan(a) - 反三角
                                add(a,b) - 两数组各元素相加
                                substract(a,b) - 相减
                                multiply(a,b) - 想乘
                                divide(a,b) - 相除
                                power(a,b) - a各元素对应的b各元素次方
                                dot(a,b) - 数组点乘（或标量普通乘）
            广播机制
            关系运算：np.greater(a b) - 相当于>,a各元素是否大于b对应的元素
                              np.greater_equal(a b) - 相当于>=
                              np.less(a b) - 相当于<
                              np.less_equal(a b) - 相当于<=
                              np.equal(a b) - 相当于==
                              np.not_equal(a b) - 相当于！=
            逻辑运算：np.any()
                              np.all()
                              np.where(condition,x,y) - 条件成立，返回x，否则y
            数组排序：np.sort()、np.argsort() - 后者返回索引
            统计运算：ndarray.max(axis) - 返回数组中最大值，指定轴axis
                              ndarray.argmax() - 返回最大值元素索引
                              ndarray.min() - 返回最小值
                              ndarray.argmin() - 返回最小值索引
                              ndarray.ptp() - 计算最大、最小值之差
                              ndarray.sum() - 求和
                              ndarray.cumsum() - 累计和
                              ndarray.mean() - 求均值
                              ndarray.var() - 求方差
                              ndarray.std() - 求标准差
                              ndarray.prod() - 计算数组元素乘积
                              ndarray.cumprod() - 计算累积
                              ndarray.trace() - 对角线之和
            线性代数运算：
                              np.linalg.det() - 行列式计算
                              np.linalg.eig() - 返回特征值和特征向量
                              np.linalg.eig() - inv(A)
                              np.solve(A,b) - 求解线性方程组AX=b
                举例：x - 2y + z = 0, 2y - 8z = 8, -4x + 5y +9z = -9
                    求解：A = np.array([[1,-2,1],[0,2,-8],[-4,5,9]])
                               b = np.array([0,8,-9])
                               x = np.linalg.solve(A,b)
                    点乘验证：np.dot(A,x)
'''

