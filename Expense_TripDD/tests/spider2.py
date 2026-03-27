import requests
from lxml import etree
import json

from sqlalchemy.util.langhelpers import repr_tuple_names


# 请求数据的过程
def request_data(url):
    headers = {
        'User-Agent': 'Mozilla/5:0 (Windows NT 10.0:Win64: x64) AppleWebKit/537.36(KHTML.1ike Gecko)Chrome/91.0.4472.114 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    with open('music.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    # 请请求到的html字符串返回
    return response.text


# 解析函数
def parse_data(html_string):
    root = etree.HTML(html_string)
    ul_list = root.xpath('//div[@class="songList"]/ul')
    print(ul_list)
    song_list = []
    for ul_node in ul_list:
        li_list = ul_node.xpath('./li')
    for li_node in li_list:
        song_list.append('name', li_node.xpath('./a/text()')[0],
                         'href', li_node.xpath('./a/@href')[0])
        return song_list


def save_data(items):
    fp = open('music.csv', 'w', encoding='utf-8')
    for item in items:
        json_string = json.dumps(item, ensure_ascii=False)
        fp.write(json_string + '\n')
    fp.close


if __name__ == '__main__':
    html_string = request_data('https://www.baidu.com/')
    # with open('music.html', 'r', encoding='utf-8') as fp:
    #     html_string = fp.read()
    song_list = parse_data(html_string)
    save_data(song_list)
