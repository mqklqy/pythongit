import requests
import json
import os

from tests.spider2 import save_data


def request_data(url):
    response = requests.get(url=url, headers=headers)

    content = response.text
    # print(content)
    return content[len('getLiveListJsonpCallback('):-1]


def parse_date(json_string):
    result_list = []
    josn_obj = json.loads(json_string)
    # print(josn_obj)
    meizi_list = josn_obj['data']['datas']
    for meizi in meizi_list:
        result_list.append({
            'nick': meizi['nick'],
            'img': meizi['screenshot']})
    return result_list

def save_data(result_list,user_path):
    if not os.path.exists(user_path):
        os.mkdir(user_path)

    for result in result_list:
        img_url = result['img']
        response=requests.get(img_url)
        file_name = result['nick']+'.jpg'
        file_path = os.path.join(user_path, file_name)
        with open(file_path, 'wb') as fp:
            fp.write(response.content)

# with open()
if __name__ == '__main__':
    url = "https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2168&tagAll=0&callback=getLiveListJsonpCallback&page=1"

    headers = {
        'User-Agent': 'Mozi1la/5.0 (Windows NT 10.0:Win64; x64)AppleWebKit/537.36(KHTML,1ike Gecko)Chrome/91.0.4472.114Safari/537.36'}
    json_string = request_data(url, headers)
    result_list = parse_date(json_string)
    save_data(result_list,'huyapath')