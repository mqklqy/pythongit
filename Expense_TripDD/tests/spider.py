import requests
from lxml import etree
import csv

url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
# print(response.text)
# with open('baidu.html','w',encoding='utf-8') as fp:
#     fp.write(html_string)
root = etree.HTML(response.text)

numbers = root.xpath('//div[@id="s-hotsearch-wrapper"]/ul/li/a/span[@style="display: ;"  or @style="display: none;"]/text()')
print(numbers)
names = root.xpath('//div[@id="s-hotsearch-wrapper"]/ul/li/a/span[@class="title-content-title"]/text()')
print(names)

# for name in names:
#     print(name)
info = []
for i in range(len(names)):
    info.append([numbers[i],names[i]])
# print(info)
fieldnames = ['numbers', 'names']
f = open('test1.csv', 'w', encoding='utf-8-sig')
f_csv = csv.writer(f)
f_csv.writerows(info)
f.close()

# from urllib.request import Request
# from urllib.request import urlopen
#
#
# url='https://www.baidu.com'
# request = Request(url)
#
# response=urlopen(request)
# # print(response.read().decode('utf-8'))
#
# html_string=response.read().decode('utf-8')
#
# with open('baidu.html','w',encoding='utf-8') as fp:
#     fp.write(html_string)
