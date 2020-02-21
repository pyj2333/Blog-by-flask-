# 登录登出首页设计

from flask import Blueprint

user = Blueprint(name="user", import_name= __name__)

# 不太明白为什么此处要导入views
from . import views

