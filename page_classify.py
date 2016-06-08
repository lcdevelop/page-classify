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
from sklearn import metrics
from sklearn.svm import SVC
from conn import Conn

conn = Conn().getConnection()

def get_segment(all=False):
    cursor = conn.cursor()

    if True == all:
        # 找到全部文章的标题和内容
        sql = "select id, title, content from CrawlPage"
    else:
        # 找到尚未切词的文章的标题和内容
        sql = "select id, title, content from CrawlPage where segment is null"
    cursor.execute(sql)

    for row in cursor.fetchall():
        print "cutting %s" % row[1]
        # 对标题和内容切词
        seg_list = jieba.cut(row[1]+' '+row[2])
        line = ""
        for str in seg_list:
            line = line + " " + str
        line = line.replace('\'', ' ')

        # 把切词按空格分隔并去特殊字符后重新写到数据库的segment字段里
        sql = "update CrawlPage set segment='%s' where id=%d" % (line, row[0])
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception,e:
            print line, e
            sys.exit(-1)

def classify():
    cursor = conn.cursor()

    # 一共分成5类，并且类别的标识定为0，1，3，4，5
    category_ids = range(0, 5)
    category={}
    category[0] = 'isTec'
    category[1] = 'isSoup'
    category[2] = 'isML'
    category[3] = 'isMath'
    category[4] = 'isNews'

    corpus = []
    for category_id in category_ids:
        # 找到这一类的所有已分类的文章并把所有切词拼成一行，加到语料库中
        sql = "select segment from CrawlPage where " + category[category_id] + "=1"
        cursor.execute(sql)
        line = ""
        for result in cursor.fetchall():
            segment = result[0]
            line = line + " " + segment
        corpus.append(line)

    # 把所有未分类的文章追加到语料库末尾行
    sql = "select id, title, segment from CrawlPage where isTec=0 and isSoup=0 and isML=0 and isMath=0 and isNews=0"
    cursor.execute(sql)
    line = ""
    update_ids = []
    update_titles = []
    need_predict = False
    for result in cursor.fetchall():
        id = result[0]
        update_ids.append(id)
        title = result[1]
        update_titles.append(title)
        segment = result[2]
        corpus.append(segment)
        need_predict = True

    if False == need_predict:
        return

    # 计算tf-idf
    vectorizer=CountVectorizer()
    csr_mat = vectorizer.fit_transform(corpus)
    transformer=TfidfTransformer()
    tfidf=transformer.fit_transform(csr_mat)
    y = np.array(category_ids)

    # 用前5行已标分类的数据做模型训练
    model = SVC()
    model.fit(tfidf[0:5], y)

    # 对5行以后未标注分类的数据做分类预测
    predicted = model.predict(tfidf[5:])

    # 把机器学习得出的分类信息写到数据库
    for index in range(0, len(update_ids)):
        update_id = update_ids[index]
        predicted_category = category[predicted[index]]
        print "predict title: %s <==============> category: %s" % (update_titles[index], predicted_category)
        sql = "update CrawlPage set %s=1 where id=%d" % (predicted_category, update_id)
        cursor.execute(sql)

    conn.commit()

if __name__ == '__main__':
    # 切词
    get_segment()
    # 分类
    classify()
    conn.close()
