# 注册蓝图
import user
import admin
import main
def register_buleprint(app):
    app.register_blueprint(user.user)
    app.register_blueprint(main.main)
    app.register_blueprint(admin.admin)


