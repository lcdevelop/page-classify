# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import matplotlib.pyplot as plt
import numpy as np

def draw(plt):
    plt.axis([-12, 12, -1, 1]) # x轴范围-12到12，y轴范围-1到1
    plt.grid(True) # 是否绘制网格线
    xx = np.linspace(-12, 12, 1000) # 在-12到12之间生成1000个点的向量
    plt.plot(xx, np.sin(xx), 'g-', label="$sin(x)$") # 绘制y=sin(x)图像，颜色green，形式为线条
    plt.plot(xx, np.cos(xx), 'r--', label="$cos(x)$") # 绘制y=cos(x)图像，颜色red，形式为虚线
    plt.legend() # 绘制图例

plt.figure() # 实例化作图变量
plt1 = plt.subplot(2,2,1) # 两行两列中的第1张图
draw(plt1)
plt2 = plt.subplot(2,2,2) # 两行两列中的第2张图
draw(plt2)
plt3 = plt.subplot(2,2,3) # 两行两列中的第3张图
draw(plt3)
plt4 = plt.subplot(2,2,4) # 两行两列中的第4张图
draw(plt4)

plt.show() # 展示图像
