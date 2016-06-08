from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

X = [[1],[10],[19]]
y = [[1],[8],[19]]

model = LinearRegression()
model.fit(X, y)

xx = np.linspace(0, 26, 100)
yy = model.predict(xx.reshape(xx.shape[0],1))
plt.figure()
plt.title('linear sample')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0, 26, 0, 26])
plt.grid(True)
plt.plot(xx,yy,'k.')
plt.show()
