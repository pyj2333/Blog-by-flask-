# 现在暂时不写前端，直接利用sql向数据中加入数据
# 只有登录后才可编辑


from . import admin
from flask import request, render_template, redirect
from moudle import db, Essay
from extension.extension import  init_time


@admin.route("/admin", methods=["POST", "GET"])
def write():
    if (request.method == "POST"):
        title = request.form["title"]
        body = request.form["body"]
        txt = Essay(title=title, body=body, user_id="1")
        db.session.add(txt)
        db.session.commit()
        return redirect("/flask/direction/")

    return render_template("/Admin/write.html")
