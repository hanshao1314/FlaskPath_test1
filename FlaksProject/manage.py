import os
from app import create,models
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from gevent import monkey   #猴子补丁

monkey.patch_all()  #猴子补丁，将当前项目中，当前代码前所有不契合地方的代码修改为契合

app = create()
manage = Manager(app)
migrate = Migrate(app,models)
app.secret_key = "123123"
app.run()
manage.add_command("db",MigrateCommand)

@manage.command
def runserver_gevent():
    """
    当前代码用于io频繁的flask项目，可以提高flask项目的效率
    :return:
    """
    from gevent import pywsgi   #gevent自带的web uwsgi 服务
    server=pywsgi.WSGIServer(("127.0.0.1",5000),app)  #封装服务
    server.server_forever()  #启动服务

if __name__ == "__main__":
    manage.run()
