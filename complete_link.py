# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import MySQLdb
import re
from conn import Conn
from elasticsearch import Elasticsearch


def FindToken(cutlist, char):
    if char in cutlist:
        return True
    else:
        return False

def Cut(cutlist,lines):
    l = []
    line = []

    for i in lines:
        if FindToken(cutlist,i):
            l.append("".join(line))
            l.append(i)
            line = []
        else:
            line.append(i)
    return l

def FindLongestSentence(lines):
    cutlist = "\/[。，,！……!《》<>\"':：？\?、\|“”‘’；]{}（）{}【】()｛｝（）：？！。，;、~——+％%`:“”＂'‘\n\r".decode('utf8')
    l = Cut(list(cutlist),list(lines.decode('utf8')))
    longest_sentence = ""
    max_len = 0
    for line in l:
        if line.strip() <> "":#这里可能包含空格
            li = line.strip().split()
            for sentence in li:
                if len(sentence) > max_len:
                    max_len = len(sentence)
                    longest_sentence = sentence

    start = lines.decode('utf8').find(longest_sentence)
    end = start + max_len
    utf8_lines = lines.decode('utf8')
    pre = utf8_lines[0:start]
    after = utf8_lines[end:]
    return pre, longest_sentence, after

def removeIllegalChar(line):
    return re.sub('\[|\]|\/|\'|\"|\(|\)|\!|\?|\~','',line)

es = Elasticsearch()

conn = Conn().getConnection()
cursor = conn.cursor()
upcursor = conn.cursor()
sql = "select id, title, substring_index(content,'相关原创文章,敬请关注',1) from CrawlPage where content not like '%</a>%'"
cursor.execute(sql)
for row in cursor.fetchall():
    id = row[0]
    title = row[1]
    content = row[2]
    title = re.sub('\[|\]|\/|\'|\"|\(|\)|\!|\?|\~|\-','',title)

    try:
        res = es.search(index="app", body={"fields":["title"],"size":1,"query": {"query_string": {"query":title}}})
        for hit in res['hits']['hits']:
            print "process:", id, title
            pre, sentence, after = FindLongestSentence(content)
            middle = len(sentence) / 2
            left = sentence[0:middle]
            right = sentence[middle:]
            new_content = "%s%s%s%s%s%s%s%s%s" % (
                    removeIllegalChar(pre),
                    removeIllegalChar(left),
                    "<a href='http://www.shareditor.com/blogshow/?blogId=",
                    hit['_id'],
                    "'>",
                    hit['fields']['title'][0],
                    "</a>",
                    removeIllegalChar(right),
                    removeIllegalChar(after))
            update_sql = "update CrawlPage set content=\"%s\" where id=%d" % (new_content, id)
            upcursor.execute(update_sql)
            conn.commit()

    except Exception,e:
        print "Error:"
        print title
        print e
        sys.exit(-1)
