# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
xx = np.linspace(0, 5, 10) # 在0-5之间生成10个点的向量
yy = np.linspace(0, 5, 10) # 在0-5之间生成10个点的向量
zz1 = xx
zz2 = 2*xx
zz3 = 3*xx
ax.scatter(xx, yy, zz1, c='red', marker='o') # o型符号
ax.scatter(xx, yy, zz2, c='green', marker='^') # 三角型符号
ax.scatter(xx, yy, zz3, c='black', marker='*') # 星型符号
ax.legend()

plt.show()
