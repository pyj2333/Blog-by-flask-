# 博客主页
# 从数据库里提取数据展示


from flask import Blueprint

main = Blueprint(name="main", import_name= __name__, url_prefix="/flask")

# 不太明白为什么此处要导入views
from . import views



