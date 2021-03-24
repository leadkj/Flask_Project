#coding:utf-8
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
import redis

from config import config_map
from .utils.commons import ReConverter

#数据库
db = SQLAlchemy()
#redis
redis_db = None
#创建日志handler
file_log_handler = RotatingFileHandler("log/log",maxBytes=1024*100,backupCount=10)
#创建日志格式
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
#handler绑定格式
file_log_handler.setFormatter(formatter)
#为全局日志对象添加handler
logging.getLogger().addHandler(file_log_handler)
#设置日志记录等级
logging.basicConfig(level=logging.DEBUG) #如果在开发模式下，强制debug级别


def create_app(config_name):
    """
    根据不同的配置创建flask 应用
    :param config_name: str  {"develop","production"}
    :return:
    """
    app = Flask(__name__)
    config = config_map.get(config_name)
    app.config.from_object(config)
    #初始化数据库
    db.init_app(app)

    #初始化redis db
    global redis_db
    redis_db = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)

    # flask-session 将session 保存到redis
    Session(app)

    # flask 添加csrf 防护
    CSRFProtect(app)

    #为flask 添加url 正则匹配
    app.url_map.converters["re"]=ReConverter

    #注册蓝图
    from flask_project import api_1_0 #防止循环导包，推迟导入
    app.register_blueprint(api_1_0.api,url_prefix="/api/v1.0")
    return  app
