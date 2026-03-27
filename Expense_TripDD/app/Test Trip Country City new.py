import requests
from flask import Flask, request, jsonify
from config import config
import dataconnection
import pymysql

# 接口URL，需替换为真实地址
# Ticket_URL = "https://ct.ctrip.com/SwitchAPI/Order/Ticket"
# GetCountry_URL = "https://ct.ctrip.com/corpopenapi/HotelCity/GetCountry"
# GetCountryCityExtend_URL = "https://ct.ctrip.com/corpopenapi/HotelCity/GetCountryCityExtend"
# 请求参数
# Ticket_data = {
#     "appKey": "obk_gokinsolar",  # 需替换为真实的接入账号
#     "appSecurity": "bW3%0!s0I~ibDzm~~UQ!eQeY"  # 需替换为真实的接入密码
# }
# 初始化Flask应用
app = Flask(__name__)
# 加载配置（默认开发环境）
app.config.from_object(config['default'])


def get_ticket():
    # 获取Ticket
    ticket_url = app.config['TICKET_URL']
    # print(ticket_url)
    # 请求参数
    ticket_data = {
        "appKey": app.config['APPKEY'],  # 需替换为真实的接入账号
        "appSecurity": app.config['APPSECURITY']  # 需替换为真实的接入密码
    }
    try:
        response = requests.post(ticket_url, data=ticket_data)
        if response.status_code == 200:
            # 解析返回的JSON数据
            result = response.json()
            ticket = result.get('Ticket')
            status = result.get('Status')
            success = status.get('Success')
            message = status.get('Message')
            error_code = status.get('ErrorCode')
            # print(f"Ticket: {ticket}")
            # print(f"调用是否成功: {success}")
            if not success:
                print(f"错误消息: {message}")
                print(f"错误编号: {error_code}")
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except requests.RequestException as e:
        print(f"请求异常: {e}")
    return ticket


# 获取国家GetCountry
def get_country():
    country_url = app.config['COUNTRY_URL']
    ticket = get_ticket()
    country_json = {
        "Auth": {
            "AppKey": app.config['APPKEY'],  # 需替换为真实的接入账号
            "Ticket": ticket
        }
    }
    try:
        response = requests.post(country_url, json=country_json)
        if response.status_code == 200:
            # 解析返回的JSON数据
            result = response.json()
            # json_str = json.dumps(result)
            # print(result)
            # print("JSON 对象：", json.dumps(result, indent=2, ensure_ascii=False))
            # Country = result.get('Country')
            # CountryEName = result.get('CountryEName')
            # CountryName = result.get('CountryName')

            status = result.get('Status')
            success = status.get('Success')
            message = status.get('Message')
            error_code = status.get('ErrorCode')
            # print(f"调用是否成功: {success}")

            country_list = result["Data"]
            print(f"\n共获取{len(country_list)}个国家：")
            # for country_list in country_list:
            #     # print(f"- {country_list.get('CountryName')}（ID：{country_list.get('Country')})")
            #     if country_list.get('CountryName') == "澳大利亚":
            #         print(f"- {country_list.get('CountryName')}（ID：{country_list.get('Country')})")
            #         countryname=country_list.get('CountryName')
            #         countryid = country_list.get('Country')
            #         print(countryid)
            if not success:
                print(f"错误消息: {message}")
                print(f"错误编号: {error_code}")
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except requests.RequestException as e:
        print(f"请求异常: {e}")
    return country_list


# 获取城市GetCountryCityExtend
def getcountrycityextend(countryid):
    countrycityextend_URL = app.config['COUNTRYCITYEXTEND_URL']
    ticket = get_ticket()
    countrycityextend_json = {
        "CountryId": countryid,
        "Auth": {
            "AppKey": app.config['APPKEY'],
            "Ticket": ticket
        }
    }
    try:
        response = requests.post(countrycityextend_URL, json=countrycityextend_json)
        if response.status_code == 200:
            # 解析返回的JSON数据
            result = response.json()
            # print(result)
            status = result.get('Status')
            success = status.get('Success')
            message = status.get('Message')
            error_code = status.get('ErrorCode')
            # print(f"调用是否成功: {success}")

            # 提取并输出城市列表（可选）
            # if result.get("Status") == "Success" and "Data" in result:
            city_list = result["Data"]
            # 处理国家-皮特凯恩群岛-城市为NUL异常情况
            if str(city_list) == 'None':
                city_list = []
            print(f"\n共获取{len(city_list)}个城市：")
            if not success:
                print(f"错误消息: {message}")
                print(f"错误编号: {error_code}")
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except requests.RequestException as e:
        print(f"请求异常: {e}")
    return city_list


if __name__ == '__main__':
    # 获取Ticket
    # ticket = get_ticket()
    # print(ticket)
    # 连接数据库
    # connection = None
    # cursor = None
    # try:
    #     connection = dataconnection.get_db_connection()
    #     if not connection:
    #         # return jsonify({'error': '数据库连接失败'}), 500
    #         print('error', '数据库连接失败')
    #     cursor = connection.cursor()
    #     # 使用 execute() 方法执行 SQL，如果表存在则删除
    #     cursor.execute("DROP TABLE IF EXISTS prod_mjb.cux_country_city")
    #     # 使用预处理语句创建表
    #     sql = """create table prod_mjb.cux_country_city
    #                     (
    #                         City VARCHAR(255) NOT NULL COMMENT '城市id',
    #                         CityEName VARCHAR(255) NOT NULL COMMENT '城市英文名称',
    #                         CityName VARCHAR(255) NOT NULL COMMENT '城市中文名称',
    #                         JianPin VARCHAR(255) NOT NULL COMMENT '城市简拼',
    #                         Country VARCHAR(255) NOT NULL COMMENT '国家id',
    #                         CountryEName VARCHAR(255) NOT NULL COMMENT '国家英文名称',
    #                         CountryName VARCHAR(255) NOT NULL COMMENT '国家中文名称',
    #                         Province VARCHAR(255) NOT NULL COMMENT '省份id',
    #                         ProvinceEName VARCHAR(255) NOT NULL COMMENT '省份英文名称',
    #                         ProvinceName VARCHAR(255) NOT NULL COMMENT '省份中文名称'
    #
    #                     )"""
    #     cursor.execute(sql)
    #     print('重建表成功')
    # except Exception as e:
    #     if connection:
    #         connection.rollback()
    #     app.logger.error(f"创建数据失败：{str(e)}")
    #     # return jsonify({'error': '创建数据失败', 'detail': str(e)}), 500
    #     print('创建数据失败errordetail', str(e))
    # 获取国家GetCountry
    countrylist = get_country()
    for country in countrylist:
        countryid = country.get('Country')
        countryname = country.get('CountryName')
        print(countryname, countryid)
        # 获取指定国家城市
        # if countryname == '澳大利亚':
        #     print(country.get('CountryName'), country.get('Country'))
        #     #countryid = country.get('Country')
        #     break
        # else:
        #     continue

        # 获取城市GetCountryCityExtend
        citylist = getcountrycityextend(countryid)
        for city in citylist:
            cityId = city.get("City", "未知")
            cityEName = city.get("CityEName", "未知")
            cityName = city.get("CityName", "未知")
            country = city.get("Country", "未知")
            countryEName = city.get("CountryEName", "未知")
            countryName = city.get("CountryName", "未知"),
            jianPin = city.get("JianPin", "未知")
            province = city.get("Province", "未知")
            provinceEName = city.get("ProvinceEName", "未知")
            provinceName = city.get("ProvinceName", "未知")
            print(cityId, cityEName, cityName, country, countryEName, countryName, jianPin, province,
                  provinceEName, provinceName)
            # SQL 插入语句
    #         sql = """INSERT INTO prod_mjb.cux_country_city
    #                 (city,
    #                 cityename,
    #                 cityname,
    #                 country,
    #                 countryename,
    #                 countryname,
    #                 jianpin,
    #                 province,
    #                 provinceename,
    #                 provincename)
    #                 VALUES
    #                 (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    #         cursor.execute(sql, (cityId, cityEName, cityName, country, countryEName, countryName, jianPin, province,
    #                              provinceEName, provinceName))
    #     # #提交到数据库执行 一个国家一提交
    #     connection.commit()
    # # 关闭数据库连接
    # dataconnection.close_db_connection(connection, cursor)
