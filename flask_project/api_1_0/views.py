#coding:utf-8
from flask import current_app, jsonify, session

from . import api

from ..utils.commons import login_required

#正则url
@api.route("/<re(r'.*'):name>")
def args(name):
    current_app.logger.error("heheheh")
    return jsonify(errno=200,errmsg=name)


@api.route("/index")
def index():
    current_app.logger.error("heheheh")
    return jsonify(errno=200,errmsg="index page")

@api.route("/session",methods=['POST'])
def login():
    #验证
    if not all(["username","password"]):
        return jsonify(errno=200, errmsg="登录成功")
    else:
        #session['username']=user.username
        #session['userid']=user.id
        return jsonify(errno=200,errmsg="登录成功")

@api.route("/session",methods=['DELETE'])
def logout():
    session.clear()
    return jsonify(errno=200,errmsg="退出")

@api.route("/goods/<id>/")
@login_required
def goods(id):
    return jsonify(errno=200,errmsg="goods1")