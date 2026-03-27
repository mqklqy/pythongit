import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import csv
import re

from sqlalchemy import true
from sqlalchemy.util.langhelpers import repr_tuple_names


# 请求数据的过程
def request_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36 Edg/146.0.0.0'}
    response = requests.get(url=url, headers=headers)
    # with open('rate.html', 'w', encoding='utf-8') as fp:
    #     fp.write(response.text)
    # 请请求到的html字符串返回
    return response.text


# 解析函数
def parse_data(html_string):
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_string, 'html.parser')
    # print(soup)
    # 查找所有表格标签
    tables = soup.find_all('table')
    # print(tables)
    rate_list = []

    for idx, table in enumerate(tables):

        if idx == 4:
            # 遍历表格的每一行
            # print(table.find_all('tr')[3])#.find_all('td')[1].text)
            cells = table.find_all('tr')
            # print(cells)
            for row in cells:
                table_data = []
                # print(row.find_all('th'))
                cells_h = row.find_all('th')
                if cells_h:
                    for cell_h in cells_h:
                        # print(cell.get_text())
                        # print(cell_h.get_text(strip=True))
                        table_data.append(cell_h.get_text(strip=True))
                        # print(f"表格 {idx + 1} 共 {len(table_data)} 行")
                else:
                    # 1外币折算成XX人民币
                    cells = row.find_all('td')
                    i = 0
                    for cell in cells:
                        # 去除首尾空白字符
                        c = cell.get_text(strip=True).strip()
                        i = i + 1
                        if '.' in c and i <= 11:
                            c = float(c) / 100
                        elif '.' in c and i > 11:
                            c = 100 / float(c)

                        # print(c)
                        table_data.append(c)
                rate_list.append(table_data)
            # print(rate_list)
    return rate_list


def save_data(items):
    fp = open('rate.csv', 'w', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(fp)
    csv_writer.writerows(items)
    fp.close


if __name__ == '__main__':
    html_string = request_data('https://www.safe.gov.cn/AppStructured/hlw/RMBQuery.do')
    song_list = parse_data(html_string)
    save_data(song_list)
    # 数据
    # data = [
    #     ["姓名", "年龄", "城市"],
    #     ["张三", 28, "北京"],
    #     ["李四", 32, "上海"]
    # ]
    #
    # # 写入CSV文件，指定编码为utf-8
    # with open('rate.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    #     writer = csv.writer(csvfile,quoting=csv.QUOTE_NONE)
    #     writer.writerows(data)
