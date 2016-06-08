# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import jieba
from jieba import analyse
import MySQLdb
import numpy as np

conn = MySQLdb.connect(host="127.0.0.1",user="lichuang",passwd="qwerty",db="sharenote2.0",charset="utf8")

def get_segment():
    cursor = conn.cursor()
    sql = "select id, title, content from CrawlPage"
    cursor.execute(sql)
    jieba.analyse.set_stop_words("stopwords.txt")
    for result in cursor.fetchall():
        id = result[0]
        content = result[1] + ' ' + result[2]
        seg_list = jieba.cut(content)
        line = ""
        for str in seg_list:
            line = line + " " + str
        line = line.replace('\'', ' ')
        sql = "update CrawlPage set segment='%s' where id=%d" % (line, id)
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception,e:
            print line
            print e
            sys.exit(-1)
    conn.close()

def feature_dump():
    cursor = conn.cursor()
    category={}
    category[0] = 'isTec'
    category[1] = 'isSoup'
    category[2] = 'isML'
    category[3] = 'isMath'
    category[4] = 'isNews'

    corpus=[]
    for index in range(0, 5):
        sql = "select segment from CrawlPage where " + category[index] + "=1"
        print sql
        cursor.execute(sql)
        line = ""
        for result in cursor.fetchall():
            segment = result[0]
            line = line + " " + segment
        corpus.append(line)

    conn.commit()
    conn.close()

    vectorizer=CountVectorizer()
    csr_mat = vectorizer.fit_transform(corpus)
    transformer=TfidfTransformer()
    tfidf=transformer.fit_transform(csr_mat)
    word=vectorizer.get_feature_names()
    print tfidf.toarray()

    for index in range(0, 5):
        f = file("tfidf_%d" % index, "wb")
        for i in np.argsort(-tfidf.toarray()[index]):
            if tfidf.toarray()[index][i] > 0:
                f.write("%f %s\n" % (tfidf.toarray()[index][i], word[i]))
        f.close()

def feature_extraction():
    d = {}
    for index in range(0, 5):
        f = file("tfidf_%d" % index, "r")
        lines = f.readlines()
        for line in lines:
            word = line.split(' ')[1][:-1]
            tfidf = line.split(' ')[0]
            if d.has_key(word):
                d[word] = np.append(d[word], tfidf)
            else:
                d[word] = np.array(tfidf)

        f.close();
    f = file("features.txt", "wb")
    for word in d:
        if d[word].size >= 2:
            index = np.argsort(d[word])
            if float(d[word][index[d[word].size-0-1]]) - float(d[word][index[d[word].size-1-1]]) > 0.01:
                f.write("%s %s\n" % (word, d[word]))
    f.close()

if __name__ == '__main__':
    #get_segment();
    feature_dump();
    feature_extraction();
