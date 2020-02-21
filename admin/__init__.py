# 网站后台
# 向数据库中写入数据


from flask import Blueprint

admin = Blueprint(name="admin", import_name= __name__, url_prefix="/fizz")

# 不太明白为什么此处要导入views
from . import views

