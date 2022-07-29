# -*- coding:utf-8 -*-
# @Time : 2022/7/28 9:57 下午
# @Author : Bin Bin Xue
# @File : project1_图像处理
# @Project : python_data_analysis

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
pic = Image.open("flower.jpeg")

# 将图片读入数组
im = np.array(pic)
print(im.shape,im)

# 用plt模块显示图像
plt.imshow(pic)
plt.show()

# 功能1_灰度处理(使用灰度计算公式计算RGB)
R = im[:,:,0]
G = im[:,:,1]
B = im[:,:,2]
# 灰度计算公式
L = R * 299/1000 + G * 587/1000 + B*114/1000
plt.imshow(L,cmap='gray')
plt.show()

# 功能2_改变图形横纵方向(交换数组的0轴和1轴)
plt.imshow(im.transpose(1,0,2))
plt.show()

# 功能3_图形翻转
# 实现纵向翻转（数组0轴整体翻转）
im_x=im[::-1]
plt.imshow(im_x)
plt.show()
# 实现横向翻转（数组1轴整体翻转）
im_y=im[:,::-1]
plt.imshow(im_y)
plt.show()

# 功能4_图形裁剪（在0轴和1轴进行切片即可）
plt.imshow(im[250:420,660:850])
plt.show()

# 功能5_图形拼接（通过数组合并）
t1 = np.concatenate((im,im),axis=1)
t2 = np.concatenate((t1,t1),axis=0)
plt.imshow(t1)
plt.show()
plt.imshow(t2)
plt.show()

# 功能6_图形分割（通过数组垂直/水平分割实现）
t1,t2,t3 = np.vsplit(im,[250,500])
plt.imshow(t1)
plt.show()
plt.imshow(t2)
plt.show()
plt.imshow(t3)
plt.show()