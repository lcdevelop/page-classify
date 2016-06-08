# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from sklearn.feature_extraction import DictVectorizer
onehot_encoder = DictVectorizer()
instances = [{'city': '北京'},{'city': '天津'}, {'city': '上海'}]
print(onehot_encoder.fit_transform(instances).toarray())
