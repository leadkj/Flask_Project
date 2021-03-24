#coding:utf-8
import functools

from flask import session, jsonify, g
from werkzeug.routing import BaseConverter

#定义url正则转换器
class ReConverter(BaseConverter):
    """"""
    def __init__(self,url_map,regex):
        super(ReConverter,self).__init__(url_map)
        self.regex = regex



#登录验证装饰器
def login_required(view_func):
    @functools.wraps(view_func)
    def warper(*args,**kwargs):
        userid = session.get("userid")
        if userid is not None:
            g.userid = userid #在一次请求中多个函数传递参数可用用g对象
            return view_func(*args,**kwargs)
        else:
            return jsonify(errno=401,errmsg="用户未登录")
    return warper
