from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash as hash
from datetime import  datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    essays = db.relationship("Essay", backref = "user", lazy = "dynamic")
    def hash_password(self, psw):  # 前端传来的密码入库前加密
        self.password = hash(psw)

    def verify_psw(self, psw):
        return hash(psw) == self.password  # 前端传来的密码与数据库中密码对比


class Essay(db.Model):
    __tablename__ = "essay"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(100), unique=False)
    body = db.Column(db.Text, unique=False)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)# 默认时间是当前时间
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

