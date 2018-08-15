from bs4 import BeautifulSoup
# import lxml
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,'lxml')
# print(soup)
# print(soup.p)
# print(type(soup.title))
# print(soup.title.name)
# print(soup.a.attrs)
# print(soup.p.attrs)
# # print(soup.a)
# print(soup.a['class'])
# print(soup.a['href'])
# print(soup.p.b)
# print(soup.find_all('a')[0])
# print(soup.title.string)
# print(type(soup.title.string))
# print(soup.title.text)
# # print(soup.title.strings)
# for i in soup.strings:
#     print(i)
# for i in soup.stripped_strings:
#     print(i)
# print(soup.name)

# html = '<b><!--这是注释文字--></b>'
# soup1 = BeautifulSoup(html,'lxml')
# comment = soup1.b.string
# print(comment)
# print(type(comment))
# print(len(soup.body.contents))
# print(soup.body.contents)
# print(soup.body.children)
# for i in soup.body.children:
#     print(i)