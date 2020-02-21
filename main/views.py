from . import main
from flask import render_template, redirect
from moudle import Essay
from extension.extension import init_time


@main.route("/direction/")
def dir():
    txt = Essay.query.all()
    for each in txt:
        if (len(each.body) > 50):
            each.body = each.body[0:50]
        each.update_time = init_time(each.update_time)
    return render_template("/Main/main.html", essay=txt)
    # txt:类对象形成的数组
    # 每次都一下子从数据库中拿出这么多数据放到内存中，
    # 文章一多，机器绝对起飞，所以用不同的页面展示.
    # 每一个页面只展示10条记录
    # 建立关于文章的模型
    # 处理时间问题，作者问题，分页展示问题。


@main.route("/Fizz/articles/details/<int:essay_id>")
def detail(essay_id):
    essay = Essay.query.filter_by(id=essay_id).first()
    if (essay is None):
        redirect("#")#重定向到错误页面
    return  render_template("/Main/details.html", essay=essay)


@main.route("/tag/")
def tag():
    pass


@main.route("/myself")
def myself():
    pass
