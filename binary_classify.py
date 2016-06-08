# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


X = []

# 前三行作为输入样本
X.append("fuck you")
X.append("fuck you all")
X.append("hello everyone")

# 后两句作为测试样本
X.append("fuck me")
X.append("hello boy")

# y为样本标注
y = [1,1,0]

vectorizer = TfidfVectorizer()

# 取X的前三句作为输入做tfidf转换
X_train = vectorizer.fit_transform(X[:-2])

# 取X的后两句用上句生成的tfidf做转换
X_test = vectorizer.transform(X[-2:])

# 用逻辑回归模型做训练
classifier = LogisticRegression()
classifier.fit(X_train, y)

# 做测试样例的预测
predictions = classifier.predict(X_test)
print predictions
pred = [[1],[0]]
false_positive_rate, recall, thresholds = roc_curve(pred, predictions)
print false_positive_rate, recall, thresholds
roc_auc = auc(false_positive_rate, recall)
plt.plot(false_positive_rate, recall, 'b', label='AUC = %0.2f' % roc_auc)
plt.show()
