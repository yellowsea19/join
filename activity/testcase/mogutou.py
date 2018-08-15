import requests
import os
import time
from urllib import parse
class sougouImg:
    def __init__(self,searchName,i):
        self.headers={
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
        }

        self.i=48
        self.key=parse.quote(searchName)
        self.page_url=[]
        for k in range(1,int(i)+1):
            url='http://pic.sogou.com/pics?query=%s&mode=1&start=%s&reqType=ajax&reqFrom=result&tn=0'%(self.key,k*self.i)
            self.page_url.append(url)
        print(self.page_url)



    def get_response(self):
        response_list=[]
        for url in self.page_url:

            response=requests.get(url=url,headers=self.headers).json()
            # print(response)
            response_list.append(response)
        return response_list

    def get_imgurl(self,response):
        img_list=[]
        for list in response:

            for j in list['items']:
                img_url=j['pic_url']
                suffix=img_url.split('.')[-1]
                img_list.append([img_url,suffix])
        return img_list

    # def __call__(self, *args, **kwargs):
    #
    def save(self,img_list):
        m=1

        for url in img_list:
            try:
                print('正在下载第%s张图片'%m,url[0])
                response=requests.get(url=url[0],headers=self.headers)
                content=response.content
                if os.path.isdir(r'D:\sougouImg')!=True:
                    os.mkdir(r'D:\sougouImg')
                with open(r'D:/sougouImg/%s.%s'%(m,url[1]),'wb') as f:
                    f.write(content)
                f.close()
                m+=1
            except :
                print('第%s张下载失败'%m)
                m+=1
                continue
        print('下载完成')
        print('下载目录为：D:\\sougouImg')
        time.sleep(10)
if __name__=='__main__':
    # i=48
    #
    # url='http://pic.sogou.com/pics?query=%s&mode=1&start=%s&reqType=ajax&reqFrom=result&tn=0'%(self.key,i)
    a=input("请输入要搜索的文字")
    b=input("请输入要下载页数（一页为48张图片）")
    sougou=sougouImg(a,b)
    response=sougou.get_response()
    img_list=sougou.get_imgurl(response)
    print(img_list)
    sougou.save(img_list)





