# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import matplotlib.pyplot as plt
import numpy as np

plt.figure() # 实例化作图变量
plt.title('single variable') # 图像标题
plt.xlabel('x') # x轴文本
plt.ylabel('y') # y轴文本
plt.axis([0, 5, 0, 10]) # x轴范围0-5，y轴范围0-10
plt.grid(True) # 是否绘制网格线
xx = np.linspace(0, 5, 10) # 在0-5之间生成10个点的向量
plt.plot(xx, 2*xx, 'g-') # 绘制y=2x图像，颜色green，形式为线条
plt.show() # 展示图像
