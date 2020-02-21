from flask import Flask
# from .register_buleprint import re_bule
# .当前目录不被视为一个package，被视为package的条件是：入口文件所在的目录不被视为package
from register_buleprint import register_buleprint
from moudle import db




def init_db(app):
    # app.app_context().push() # 上下文推动
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()



def creat_app(config="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    register_buleprint(app)
    db.app = app
    db.init_app(app)
    return app
