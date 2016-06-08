# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline

# 构造样本，这块得多构造点，不然会报class不足的错误，因为gridsearch会拆分成小组
X = []
X.append("fuck you")
X.append("fuck you all")
X.append("hello everyone")
X.append("fuck me")
X.append("hello boy")
X.append("fuck you")
X.append("fuck you all")
X.append("hello everyone")
X.append("fuck me")
X.append("hello boy")
X.append("fuck you")
X.append("fuck you all")
X.append("hello everyone")
X.append("fuck me")
X.append("hello boy")
X.append("fuck you")
X.append("fuck you all")
X.append("hello everyone")
X.append("fuck me")
X.append("hello boy")
X.append("fuck you")
X.append("fuck you all")
X.append("hello everyone")
X.append("fuck me")
X.append("hello boy")

y = [1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1]

# 这是执行的序列，gridsearch是构造多进程顺序执行序列并比较结果
# 这里的vect和clf名字自己随便起，但是要和parameters中的前缀对应
pipeline = Pipeline([
    ('vect', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression())
    ])

# 这里面的max_features必须是TfidfVectorizer的参数, 里面的取值就是子进程分别执行所用
parameters = {
        'vect__max_features': (3, 5),
        }

# accuracy表示按精确度判断最优值
grid_search = GridSearchCV(pipeline, parameters, n_jobs = -1, verbose = 1, scoring = 'accuracy', cv = 3)
grid_search.fit(X, y)

print '最佳效果: %0.3f' % grid_search.best_score_
print '最优参数组合: '
best_parameters = grid_search.best_estimator_.get_params()
for param_name in sorted(parameters.keys()):
    print('\t%s: %r' % (param_name, best_parameters[param_name]))
