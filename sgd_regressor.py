# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

plt.figure() # 实例化作图变量
plt.title('single variable') # 图像标题
plt.xlabel('x') # x轴文本
plt.ylabel('y') # y轴文本
plt.grid(True) # 是否绘制网格线

X_scaler = StandardScaler()
y_scaler = StandardScaler()
#X = [[50],[100],[150],[200],[250],[300]]
#y = [[150],[200],[250],[280],[310],[330]]
X = [[50],[100],[150],[200],[250],[300],[50],[100],[150],[200],[250],[300],[50],[100],[150],[200],[250],[300],[50],[100],[150],[200],[250],[300],[50],[100],[150],[200],[250],[300],[50],[100],[150],[200],[250],[300],[50],[100],[150],[200],[250],[300],[50],[100],[150],[200],[250],[300]]
y = [[150],[200],[250],[280],[310],[330],[150],[200],[250],[280],[310],[330],[150],[200],[250],[280],[310],[330],[150],[200],[250],[280],[310],[330],[150],[200],[250],[280],[310],[330],[150],[200],[250],[280],[310],[330],[150],[200],[250],[280],[310],[330],[150],[200],[250],[280],[310],[330]]
X = X_scaler.fit_transform(X)
y = y_scaler.fit_transform(y)
X_test = [[40],[400]] # 用来做最终效果测试
X_test = X_scaler.transform(X_test)

plt.plot(X, y, 'k.')

model = SGDRegressor()
model.fit(X, y.ravel())
y_result = model.predict(X_test)
print y_result
plt.plot(X_test, y_result, 'g-')

plt.show() # 展示图像

