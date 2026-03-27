import requests
import pymysql

# 打开数据库连接
db = pymysql.connect(host='172.16.6.94',
                     user='root',
                     password='Ems@12345678',
                     database='uat_mjb')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS uat_mjb.cux_country_city")

# 使用预处理语句创建表
sql = """create table uat_mjb.cux_country_city
(
    City VARCHAR(255) NOT NULL COMMENT '城市id',
    CityEName VARCHAR(255) NOT NULL COMMENT '城市英文名称',
    CityName VARCHAR(255) NOT NULL COMMENT '城市中文名称',
    JianPin VARCHAR(255) NOT NULL COMMENT '城市简拼',
    Country VARCHAR(255) NOT NULL COMMENT '国家id',
    CountryEName VARCHAR(255) NOT NULL COMMENT '国家英文名称',
    CountryName VARCHAR(255) NOT NULL COMMENT '国家中文名称',
    Province VARCHAR(255) NOT NULL COMMENT '省份id',
    ProvinceEName VARCHAR(255) NOT NULL COMMENT '省份英文名称',
    ProvinceName VARCHAR(255) NOT NULL COMMENT '省份中文名称'

)"""
cursor.execute(sql)

# 接口URL，需替换为真实地址
Ticket_URL = "https://ct.ctrip.com/SwitchAPI/Order/Ticket"
GetCountry_URL = "https://ct.ctrip.com/corpopenapi/HotelCity/GetCountry"
GetCountryCityExtend_URL = "https://ct.ctrip.com/corpopenapi/HotelCity/GetCountryCityExtend"
# 请求参数
Ticket_data = {
    "appKey": "obk_gokinsolar",  # 需替换为真实的接入账号
    "appSecurity": "bW3%0!s0I~ibDzm~~UQ!eQeY"  # 需替换为真实的接入密码
}

# 获取Ticket
try:
    response = requests.post(Ticket_URL, data=Ticket_data)
    if response.status_code == 200:
        # 解析返回的JSON数据
        result = response.json()
        ticket = result.get('Ticket')
        status = result.get('Status')
        success = status.get('Success')
        message = status.get('Message')
        error_code = status.get('ErrorCode')
        print(f"Ticket: {ticket}")
        print(f"调用是否成功: {success}")
        if not success:
            print(f"错误消息: {message}")
            print(f"错误编号: {error_code}")
    else:
        print(f"请求失败，状态码: {response.status_code}")
except requests.RequestException as e:
    print(f"请求异常: {e}")
# 获取国家GetCountry
GetCountry_json = {
    "Auth": {
        "AppKey": "obk_gokinsolar",  # 需替换为真实的接入账号
        "Ticket": ticket
    }
}

try:
    response = requests.post(GetCountry_URL, json=GetCountry_json)
    if response.status_code == 200:
        # 解析返回的JSON数据
        result = response.json()
        # json_str = json.dumps(result)
        print(result)
        # print("JSON 对象：", json.dumps(result, indent=2, ensure_ascii=False))
        # Country = result.get('Country')
        # CountryEName = result.get('CountryEName')
        # CountryName = result.get('CountryName')

        status = result.get('Status')
        success = status.get('Success')
        message = status.get('Message')
        error_code = status.get('ErrorCode')
        print(f"调用是否成功: {success}")

        country_list = result["Data"]
        print(f"\n共获取{len(country_list)}个国家：")
        for country_list in country_list:
            # print(f"- {country_list.get('CountryName')}（ID：{country_list.get('Country')})")
            if country_list.get('CountryName') == "澳大利亚":#皮特凯恩群岛 澳大利亚
                print(f"- {country_list.get('CountryName')}（ID：{country_list.get('Country')})")
                CountryId = country_list.get('Country')
                print(CountryId)
        if not success:
            print(f"错误消息: {message}")
            print(f"错误编号: {error_code}")
    else:
        print(f"请求失败，状态码: {response.status_code}")
except requests.RequestException as e:
    print(f"请求异常: {e}")
# 获取城市GetCountryCityExtend
GetCountryCityExtend_json = {
    "CountryId": CountryId,
    "Auth": {
        "AppKey": "obk_gokinsolar",
        "Ticket": ticket
    }
}

try:
    response = requests.post(GetCountryCityExtend_URL, json=GetCountryCityExtend_json)
    if response.status_code == 200:
        # 解析返回的JSON数据
        result = response.json()
        # print(result)
        status = result.get('Status')
        success = status.get('Success')
        message = status.get('Message')
        error_code = status.get('ErrorCode')
        print(f"调用是否成功: {success}")

        # 提取并输出城市列表（可选）
        # if result.get("Status") == "Success" :
        #     city_list = result["Data"]
        # else:
        #     city_list=[]
        city_list = result["Data"]
        print(city_list)
        print(type(city_list))
        if str(city_list) == 'None':
            city_list = []
        city_count = len(city_list)
        print(f"\n共获取{city_count}个城市：")
        for city in city_list:
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
            # print(cityId)
            # print(cityEName)
            # print(countryName)
            # SQL 插入语句
            sql = """INSERT INTO uat_mjb.cux_country_city
  (city,
   cityename,
   cityname,
   country,
   countryename,
   countryname,
   jianpin,
   province,
   provinceename,
   provincename)
VALUES
  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            try:
                # 执行sql语句
                cursor.execute(sql, (cityId, cityEName, cityName, country, countryEName, countryName, jianPin, province,
                                     provinceEName, provinceName))
                # 提交到数据库执行
                db.commit()
            except Exception as e:
                # 如果发生错误则回滚
                db.rollback()
                print("插入数据异常", e.message)
            # print(f"- {city.get('CityName', '未知城市')}（ID：{city.get('City')})")
        # else:
        #     print(f"\n获取失败：{result.get('StatusMessage', '未知错误')}")
        if not success:
            print(f"错误消息: {message}")
            print(f"错误编号: {error_code}")
    else:
        print(f"请求失败，状态码: {response.status_code}")
except requests.RequestException as e:
    print(f"请求异常: {e}")

################################################################
# 关闭数据库连接
db.close()
print("数据插入完成")
