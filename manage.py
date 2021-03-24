#coding:utf-8
from flask_project import  create_app,db

from flask_script import Manager,Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app("develop")
def make_shell_context():
    return dict(app=app, db=db)

manager = Manager(app)
Migrate(app,db)
manager.add_command("shell", Shell(make_context=make_shell_context)) #在终端环境下添加一个shell命令
manager.add_command('db', MigrateCommand) #在终端环境下添加一个db命令


if __name__ == "__main__":
    manager.run()
