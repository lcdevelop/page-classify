# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

plt.figure() # 实例化作图变量
plt.title('single variable') # 图像标题
plt.xlabel('x') # x轴文本
plt.ylabel('y') # y轴文本
plt.axis([30, 400, 100, 400])
plt.grid(True) # 是否绘制网格线

X = [[50],[100],[150],[200],[250],[300]]
y = [[150],[200],[250],[280],[310],[330]]
X_test = [[250],[300]] # 用来做最终效果测试
y_test = [[310],[330]] # 用来做最终效果测试
plt.plot(X, y, 'k.')

model = LinearRegression()
model.fit(X, y)
X2 = [[30], [400]]
y2 = model.predict(X2)
plt.plot(X2, y2, 'g-')

xx = np.linspace(30, 400, 100) # 设计x轴一系列点作为画图的x点集
quadratic_featurizer = PolynomialFeatures(degree=2) # 实例化一个二次多项式特征实例
X_train_quadratic = quadratic_featurizer.fit_transform(X) # 用二次多项式对样本X值做变换
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1)) # 把训练好X值的多项式特征实例应用到一系列点上,形成矩阵
regressor_quadratic = LinearRegression() # 创建一个线性回归实例
regressor_quadratic.fit(X_train_quadratic, y) # 以多项式变换后的x值为输入，代入线性回归模型做训练
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), 'r-') # 用训练好的模型作图



cubic_featurizer = PolynomialFeatures(degree=3)
X_train_cubic = cubic_featurizer.fit_transform(X)
X_test_cubic = cubic_featurizer.transform(X_test)
regressor_cubic = LinearRegression()
regressor_cubic.fit(X_train_cubic, y)
xx_cubic = cubic_featurizer.transform(xx.reshape(xx.shape[0], 1))
plt.plot(xx, regressor_cubic.predict(xx_cubic))

print '一元线性回归 r-squared', model.score(X_test, y_test)
X_test_quadratic = quadratic_featurizer.transform(X_test)
print '二次回归     r-squared', regressor_quadratic.score(X_test_quadratic, y_test)
print '三次回归     r-squared', regressor_cubic.score(X_test_cubic, y_test)

plt.show() # 展示图像

