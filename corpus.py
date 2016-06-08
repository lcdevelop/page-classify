# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from sklearn.feature_extraction.text import CountVectorizer
corpus = [
        'UNC played Duke in basketball',
        'Duke lost the basketball game' ]
vectorizer = CountVectorizer()
print vectorizer.fit_transform(corpus).todense()
print vectorizer.vocabulary_
