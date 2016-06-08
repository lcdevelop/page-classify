# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import MySQLdb
from conn import Conn

begin='''<?xml version="1.0" encoding="UTF-8"?>
<urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
      http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
'''
end='</urlset>'
subbegin='  <url><loc>'
subend='</loc></url>'
conn = Conn().getConnection()

def addUrl(sitemap, url):
    return sitemap+"%s%s%s\n" % (subbegin, url, subend)

def addStaticUrl(sitemap):
    sitemap = addUrl(sitemap, 'http://www.shareditor.com/')
    sitemap = addUrl(sitemap, 'http://www.shareditor.com/bloglist/1')
    sitemap = addUrl(sitemap, 'http://www.shareditor.com/bloglist/2')
    sitemap = addUrl(sitemap, 'http://www.shareditor.com/bloglist/3')
    sitemap = addUrl(sitemap, 'http://www.shareditor.com/bloglist/4')
    sitemap = addUrl(sitemap, 'http://www.shareditor.com/bloglist/5')
    sitemap = addUrl(sitemap, 'http://favorite.shareditor.com/favorite/')
    sitemap = addUrl(sitemap, 'http://favorite.shareditor.com/favorite/categorylist?category=机器学习')
    sitemap = addUrl(sitemap, 'http://favorite.shareditor.com/favorite/categorylist?category=技术文章')
    sitemap = addUrl(sitemap, 'http://favorite.shareditor.com/favorite/categorylist?category=新闻资讯')
    sitemap = addUrl(sitemap, 'http://favorite.shareditor.com/favorite/categorylist?category=数学知识')
    sitemap = addUrl(sitemap, 'http://favorite.shareditor.com/favorite/categorylist?category=鸡汤文章')
    return sitemap

def gen_sitemap(sitemap):
    cursor = conn.cursor()
    sql = "select id from BlogPost"
    cursor.execute(sql)
    for row in cursor.fetchall():
        url='http://www.shareditor.com/blogshow/?blogId=%d' % row[0]
        sitemap = addUrl(sitemap, url)
    return sitemap

def gen_favoritesitemap(sitemap):
    cursor = conn.cursor()
    sql = "select id from CrawlPage"
    cursor.execute(sql)
    for row in cursor.fetchall():
        url='http://favorite.shareditor.com/favorite/pageshow?pageid=%d' % row[0]
        sitemap = addUrl(sitemap, url)
    return sitemap

if __name__ == '__main__':
    sitemap=begin
    sitemap=addStaticUrl(sitemap)
    sitemap=gen_sitemap(sitemap)
    sitemap=gen_favoritesitemap(sitemap)
    sitemap+=end
    print sitemap
