from flask import request, render_template
from . import user


@user.route("/")
def index():
    return render_template("/Index/index.html")


@user.route("/login", methods = ["GET", "POST"])
def login():
    if (request.method == "POST"):
        pass
    return render_template("/user/login.html")


@user.route("/register", methods = ["GET", "POST"])
def register():
    if (request.method == "POST"):
        pass
    return "register"


@user.route("/logout")
def logout():
    pass

