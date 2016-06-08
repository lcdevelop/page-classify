# coding:utf-8

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import jieba
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1",user="lichuang",passwd="qwerty",db="test",charset="utf8")
cursor = conn.cursor()

sql = "select content from page"
cursor.execute(sql)
corpus=[]
for content in cursor.fetchall():
    seg_list = jieba.cut(content[0])
    line = ""
    for str in seg_list:
        line = line + " " + str
    corpus.append(line)
conn.commit()
conn.close()

vectorizer=CountVectorizer()
csr_mat = vectorizer.fit_transform(corpus)
transformer=TfidfTransformer()
tfidf=transformer.fit_transform(csr_mat)
word=vectorizer.get_feature_names()
print tfidf.toarray()
