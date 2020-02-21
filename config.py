# 配置秘钥
SECRET_KEY='dev'

# 配置数据库
# 文件目录必须首先被建立
SQLALCHEMY_DATABASE_URI = "sqlite:///temp/test.db"
SQLALCHEMY_TRACK_MODIFICATIONS=True