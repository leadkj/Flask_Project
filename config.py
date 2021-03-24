#coding:utf-8

import redis

class Config(object):
    """配置信息"""
    DEBUG = True
    SECRET_KEY = "jfkldajf_f)(*(*fkdj-fda232jk"

    #数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/testdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    #session config
    SESSION_TYPE = "reids"
    SESSION_REIDS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USER_SIGNER = True  #对cookie中的session-id 隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400 #session 有效期，单位S

class DevelopmentConfig(Config):
    """开发环境"""
    pass

class ProductionConfig(Config):
    """生产环境"""
    DEBUG = False


config_map ={
    "develop":DevelopmentConfig,
    "production": ProductionConfig
}