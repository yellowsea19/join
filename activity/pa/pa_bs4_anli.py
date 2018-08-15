from bs4 import BeautifulSoup
import requests
from lxml import etree
url='https://hr.tencent.com/position.php'
headers={

'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

response=requests.get(url,headers=headers,verify=False)
f=response.text

# soup=BeautifulSoup(f,'lxml')
# tmplist=soup.find_all('a',target="_blank")
# for i in tmplist:
#     if 'http'not in i['href']:
#
#         print (i['href'])


soup=etree.HTML(f)

temp_list=soup.xpath('//tr[@class="even"]/td[1]|//tr[@class="odd"]/td[1]')
# print(temp_list)
for i in temp_list:
    position_name=i.xpath('./a/text()')
    print(position_name)