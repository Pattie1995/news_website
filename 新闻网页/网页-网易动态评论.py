# encoding=utf-8
import urllib.request
import json
import re
class WYTie():
    def __init__(self):
        self.user_agent='Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
        self.headers={'User-Agent':self.user_agent}
        self.url1='http://comment.news.163.com/data/news_guonei8_bbs/df/B9C8EJDC0001124J_1.html'
    def getUrl(self,pageIndex):
        url2='http://comment.news.163.com/cache/newlist/news_guonei8_bbs/B9C8EJDC0001124J_'+str(pageIndex)+'.html'
        return url2
    def getHtml(self,url):
        try:
            request=urllib.request.Request(url,headers=self.headers)
            page=urllib.request.urlopen(request)
            html=page.read()
            return html
        except urllib.request.URLError as e:
            if hasattr(e,'reason'):
                print(u"连接失败",e.reason)
                return None
    #将所有替换写成函数，在后面进行调用
    def getRaplace(self,data,i):
        if i==1:
            data=data.replace('var replyData=','')
        else:
            data=data.replace('var newPostList=','')
        rep=re.compile(" \[<a href=''>")
        data=rep.sub('--',data)
        rep2=re.compile('<\\\/a>\]')
        data=rep2.sub('',data)
        rep3=re.compile("<span(.*?)/span>")
        data=rep3.sub(' ',data)
        rep4=re.compile(";")
        data=rep4.sub(' ',data)
        return data
    #将数据转换并进行存储
    def getItems(self):
        with open('wynewsssss.txt','a') as f:
            f.write('用户名'+'|'+'评论'+'|'+'顶'+'\n')
        for pageIndex in range(1,18):
            if pageIndex==1:
                url=self.url1
                data=self.getHtml(url)
                data=self.getRaplace(data,pageIndex)
                value=json.loads(data)
                f=open('wynewsssss.txt','a')
                for item in value['hotPosts']:
                    f.write(item['1']['f'].encode('utf-8')+'|')
                    f.write(item['1']['b'].encode('utf-8')+'|')
                    f.write(item['1']['v'].encode('utf-8')+'\n')
                f.close()
            else:
                url=self.getUrl(pageIndex)
                data=self.getHtml(url)
                data=self.getRaplace(data,pageIndex)
                value=json.loads(data)
                f=open('wynewsssss.txt','a')
                for item in value['newPosts']:
                    f.write(item['1']['f'].encode('utf-8')+'|')
                    f.write(item['1']['b'].encode('utf-8')+'|')
                    f.write(item['1']['v'].encode('utf-8')+'\n')
                f.close()


spider=WYTie()
spider.getItems()
