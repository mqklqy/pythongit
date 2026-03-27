#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='172.16.6.94',
                     user='root',
                     password='Ems@12345678',
                     database='uat_mjb')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)
################################################################

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


################################################################
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
  ('12121', 'ABD', 'ABD', 'ABD', 'ABD', 'ABD', 'ABD', 'ABD', 'ABD', 'ABD')"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    # 如果发生错误则回滚
    db.rollback()
    print(f"错误: {e}")
################################################################
# 关闭数据库连接
db.close()
