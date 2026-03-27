import requests
from flask import Flask, request, jsonify
from config import config
import dataconnection
import time

# 初始化Flask应用
app = Flask(__name__)
# 加载配置（默认开发环境）
app.config.from_object(config['default'])

cityname_new = '湘西土家族苗族自治州'
area_id = '211'
area_name = '湖南省'

if __name__ == '__main__':
    # 连接数据库
    connection = None
    cursor = None
    try:
        connection = dataconnection.get_db_connection()
        if not connection:
            # return jsonify({'error': '数据库连接失败'}), 500
            print('error', '数据库连接失败')
        cursor = connection.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        print("Database version : %s " % data)
    except Exception as e:
        if connection:
            connection.rollback()
        app.logger.error(f"数据库失败：{str(e)}")
        # return jsonify({'error': '创建数据失败', 'detail': str(e)}), 500
        print('数据库连接失败errordetail', str(e))
    # 1 判断hotel_city_vendor表中是否为空，并补全数据-----------------------------
    try:
        # prod_mjb.hotel_city_vendor
        sql = """SELECT cc.*,
                                   hc.city_id,
                                   hc.city_en_name,
                                   hc.city_name,
                                   hc.short_name,
                                   hc.country_id,
                                   hc.country_en_name,
                                   hc.country_name,
                                   hc.province_id,
                                   hc.province_en_name,
                                   hc.province_name
                              FROM prod_mjb.cux_country_city cc
                              LEFT JOIN prod_mjb.hotel_city_vendor hc
                                ON 1 = 1 #and hc.city_en_name = cc.countryename
                               AND (cc.cityname = hc.city_name AND cc.country = hc.country_id AND
                                   cc.province = hc.province_id)
                             WHERE 1 = 1
                               AND hc.city_id IS NULL
                               AND cc.country = 1
                               AND cc.cityname =%s
                            """
        cursor.execute(sql, cityname_new)
        # 获取prod_mjb.hotel_city_vendor表所有记录列表
        results = cursor.fetchall()
        if results:
            print("查询1hotel_city_vendor结果：", results)
        for city in results:
            localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("本地时间为 :", localtime)
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
            print('插入数据开始')
            # SQL 插入语句
            try:
                sql = """insert	into prod_mjb.hotel_city_vendor
                                    (
                                        city_id,
                                        city_en_name,
                                        city_name,
                                        short_name,
                                        country_id,
                                        country_en_name,
                                        country_name,
                                        province_id,
                                        province_en_name,
                                        province_name,
                                        vendor_code,
                                        trip_type,
                                        created_name,
                                        created_by,
                                        creation_date,
                                        last_updated_by,
                                        last_updated_name,
                                        last_update_date
                                    )
                                VALUES
                                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, (cityId, cityEName, cityName, jianPin, country, countryEName, countryName, province,
                                     provinceEName, provinceName, 'CTRIP', 'HOTEL',
                                     '管理员01', '0', localtime, '0', '管理员01', localtime))
                # #提交到数据库执行 一个国家一提交
                connection.commit()
            except Exception as e:
                if connection:
                    connection.rollback()
                    app.logger.error(f"插入hotel_city_vendor数据失败：{str(e)}")
                print('插入hotel_city_vendor数据失败errordetail', str(e))
        else:
            print("提醒：查询1hotel_city_vendor结果为空。")
    except Exception as e:
        if connection:
            connection.rollback()
            app.logger.error(f"查询1数据失败：{str(e)}")
        # return jsonify({'error': '创建数据失败', 'detail': str(e)}), 500
        print('查询1数据失败errordetail', str(e))
    # 2 判断bd_area表中是否为空，并补全数据-----------------------------
    try:
        sql = """
                select
                    cc.*,
                    bd.*
                from
                    prod_mjb.cux_country_city cc
                left join prod_mjb.bd_area bd
                                            on
                    1 = 1
                    #and hc.city_en_name = cc.countryename
                    and (cc.cityname = bd.area_name )
                where
                    1 = 1
                    and bd.area_id  is null
                    and cc.cityname = %s
                    """
        cursor.execute(sql, cityname_new)
        # 获取prod_mjb.bd_area表所有记录列表
        results_ba = cursor.fetchall()
        if results_ba:
            print("查询2bd_area结果：", results_ba)
        for city_ba in results_ba:
            localtime_ba = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # print("本地时间为 :", localtime_ba)
            cityId = city_ba.get("City", "未知")
            cityEName = city_ba.get("CityEName", "未知")
            cityName = city_ba.get("CityName", "未知")
            country = city_ba.get("Country", "未知")
            countryEName = city_ba.get("CountryEName", "未知")
            countryName = city_ba.get("CountryName", "未知"),
            jianPin = city_ba.get("JianPin", "未知")
            province = city_ba.get("Province", "未知")
            provinceEName = city_ba.get("ProvinceEName", "未知")
            provinceName = city_ba.get("ProvinceName", "未知")
            print(cityId, cityEName, cityName, country, countryEName, countryName, jianPin, '402/' + cityId, province,
                  provinceEName, provinceName)
            # SQL 插入语句
            try:
                sql = """insert	into prod_mjb.bd_area
                                                    (
                                                        area_id ,
                                                        area_code ,
                                                        area_name ,
                                                        pin_yin ,
                                                        region_type_code ,
                                                        full_path ,
                                                        full_path_name ,
                                                        parent_area_id,
                                                        is_travel_city ,
                                                        active_flag ,
                                                        last_update_date ,
                                                        attribute1
                                                    )
                                                VALUES
                                                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql,
                               (cityId, cityId, cityName, jianPin, '3', area_id + cityId, area_name + '/' + cityName,
                                area_id,
                                'Y', 'Y', localtime_ba, jianPin))
                # #提交到数据库执行 一个国家一提交
                connection.commit()
            except Exception as e:
                if connection:
                    connection.rollback()
                    app.logger.error(f"插入bd_area数据失败：{str(e)}")
                print('插入表bd_area数据失败errordetail', str(e))
        else:
            print("提醒：查询2bd_area结果为空。")
    except Exception as e:
        if connection:
            connection.rollback()
            app.logger.error(f"查询2数据失败：{str(e)}")
        # return jsonify({'error': '创建数据失败', 'detail': str(e)}), 500
        print('查询2数据失败errordetail', str(e))
    # 3 判断buy_city_relation表中是否为空，并补全数据-----------------------------
    try:
        sql = """
            select
                cc.*,
                bc.*
            from
                prod_mjb.cux_country_city cc
            left join prod_mjb.buy_city_relation bc
                                    on
                1 = 1
                #and hc.city_en_name = cc.countryename
                and (cc.cityname = bc.vendor_city_name)
            where
                1 = 1
                and bc.vendor_city_id  is null
                and cc.cityname = %s
            """
        cursor.execute(sql, cityname_new)
        # 获取prod_mjb.buy_city_relation表所有记录列表
        results_bc = cursor.fetchall()
        if results_bc:
            print("查询3buy_city_relation结果：", results_bc)
        for city_bc in results_bc:
            localtime_bc = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # print("本地时间为 :", localtime_bc)
            cityId = city_bc.get("City", "未知")
            cityEName = city_bc.get("CityEName", "未知")
            cityName = city_bc.get("CityName", "未知")
            country = city_bc.get("Country", "未知")
            countryEName = city_bc.get("CountryEName", "未知")
            countryName = city_bc.get("CountryName", "未知"),
            jianPin = city_bc.get("JianPin", "未知")
            province = city_bc.get("Province", "未知")
            provinceEName = city_bc.get("ProvinceEName", "未知")
            provinceName = city_bc.get("ProvinceName", "未知")
            print(cityId, cityEName, cityName, country, countryEName, countryName, jianPin, area_id + cityId, province,
                  provinceEName, provinceName)
            # SQL 插入语句
            try:
                sql = """insert	into prod_mjb.buy_city_relation
                                                    (
                                                    vendor_city_id ,
                                                    vendor_city_name ,
                                                    mjb_city_id ,
                                                    mjb_city_code ,
                                                    mjb_city_name ,
                                                    vendor_code ,
                                                    trip_type 
                                                    )
                                                VALUES
                                                (%s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql,
                               (cityId, cityName, cityId, cityId, cityName, 'CTRIP', 'HOTEL'))
                # #提交到数据库执行 一个国家一提交
                connection.commit()
            except Exception as e:
                if connection:
                    connection.rollback()
                    app.logger.error(f"插入buy_city_relation数据失败：{str(e)}")
                print('插入表buy_city_relation数据失败errordetail', str(e))
        else:
            print("提醒：查询3buy_city_relation结果为空。")
    except Exception as e:
        if connection:
            connection.rollback()
            app.logger.error(f"查询2数据失败：{str(e)}")
        # return jsonify({'error': '创建数据失败', 'detail': str(e)}), 500
        print('查询2数据失败errordetail', str(e))
    # # 关闭数据库连接
    dataconnection.close_db_connection(connection, cursor)
