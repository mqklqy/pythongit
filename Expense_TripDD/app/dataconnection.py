from flask import Flask, request, jsonify
import pymysql
from config import config

# 初始化Flask应用
app = Flask(__name__)
# 加载配置（默认开发环境）
app.config.from_object(config['default'])

#print(app.config['MYSQL_HOST'])
#print(app.config['TICKET_URL'])


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
