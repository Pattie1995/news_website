import requests
import json
comments=requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-hmutuea9276660'
                      '&group=0&compress=0&ie=gbk&oe=gbk&page=1&'
                      'page_size=3&t_size=3&h_size=10&thread=1&'
                     )
comments.encoding=('utf-8')
comments.text
jd=json.loads(comments.text)
print(jd['result']['count'])
for i in range(9):
    print(jd['result']['hot_list'][i]['content'])