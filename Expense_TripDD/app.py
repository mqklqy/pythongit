from flask import Flask, request, jsonify
import pymysql
from config import config

# 初始化Flask应用
app = Flask(__name__)
# 加载配置（默认开发环境）
app.config.from_object(config['default'])

print(app.config['MYSQL_HOST'])
print(app.config['TICKET_URL'])

# 数据库连接函数
def get_db_connection():
    try:
        connection = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            port=app.config['MYSQL_PORT'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB'],
            charset=app.config['MYSQL_CHARSET'],
            cursorclass=pymysql.cursors.DictCursor  # 游标返回字典格式（便于转换为JSON）
        )
        return connection
    except pymysql.Error as e:
        app.logger.error(f"数据库连接失败：{str(e)}")
        return None


# 关闭数据库连接函数
def close_db_connection(connection, cursor):
    if cursor:
        cursor.close()
    if connection:
        connection.close()


# 新增用户
#@app.route('/api/users', methods=['POST'])
def create_city():
    data = request.get_json()
    required_fields = ['city',
                       'cityename',
                       'cityname',
                       'country',
                       'countryename',
                       'c',
                       'jianpin',
                       'province',
                       'provinceename',
                       'provincename']
    if not all(field in data for field in required_fields):
        return jsonify({'error': '缺少必填字段（city/cityname/cityname）'}), 400

    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': '数据库连接失败'}), 500

        cursor = connection.cursor()
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
        cursor.execute(sql, (cityId, cityEName, cityName, country, countryEName, countryName, jianPin, province,
                             provinceEName, provinceName))
        connection.commit()

        # user_id = cursor.lastrowid
        # cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        # new_user = cursor.fetchone()
        #
        # return jsonify({'message': '用户创建成功', 'user': new_user}), 201

    # except pymysql.IntegrityError as e:
    #     connection.rollback()
    #     return jsonify({'error': '邮箱已存在', 'detail': str(e)}), 409
    except Exception as e:
        if connection:
            connection.rollback()
        app.logger.error(f"创建数据失败：{str(e)}")
        return jsonify({'error': '创建数据失败', 'detail': str(e)}), 500
    finally:
        close_db_connection(connection, cursor)


if __name__ == '__main__':
    create_city()
   # app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
