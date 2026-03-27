import os



# 数据库连接
class Config:
    # MySQL数据库连接信息
    #测试环境
    # MYSQL_HOST = '172.16.6.94'    # 数据库主机地址（本地为127.0.0.1）
    # MYSQL_PORT = 3306           # 数据库端口（默认3306）
    # MYSQL_USER = 'root'         # 数据库用户名（根据实际情况修改）
    # MYSQL_PASSWORD = 'Ems@12345678'   # 数据库密码（根据实际情况修改）
    # MYSQL_DB = 'uat_mjb'# 数据库名（与前文创建的一致）
    ################################
    #生产环境
    MYSQL_HOST = '172.16.6.148'  # 数据库主机地址（本地为127.0.0.1）
    MYSQL_PORT = 3306  # 数据库端口（默认3306）
    MYSQL_USER = 'root'  # 数据库用户名（根据实际情况修改）
    MYSQL_PASSWORD = 'GOkin@996db'  # 数据库密码（根据实际情况修改）
    MYSQL_DB = 'prod_mjb'  # 数据库名（与前文创建的一致）
    ################################
    MYSQL_CHARSET = 'utf8mb4'   # 字符集
    TICKET_URL = 'https://ct.ctrip.com/SwitchAPI/Order/Ticket'# 携程接口URL，需替换为真实地址
    COUNTRY_URL = 'https://ct.ctrip.com/corpopenapi/HotelCity/GetCountry'
    COUNTRYCITYEXTEND_URL = 'https://ct.ctrip.com/corpopenapi/HotelCity/GetCountryCityExtend'
    #携程appKey
    APPKEY='obk_gokinsolar'  # 需替换为真实的接入账号
    APPSECURITY='bW3%0!s0I~ibDzm~~UQ!eQeY'  # 需替换为真实的接入密码

# 开发环境配置（继承Config）
class DevelopmentConfig(Config):
    DEBUG = True  # 开启调试模式

# 生产环境配置（继承Config）
class ProductionConfig(Config):
    DEBUG = False  # 关闭调试模式
    # 生产环境可添加数据库连接池配置，提升性能
    MYSQL_POOL_SIZE = 10
    MYSQL_MAX_OVERFLOW = 20

# 配置映射，方便切换环境
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
