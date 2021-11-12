from app import app
from app import create_app,db
from flask_script import Manager,Server
from flask_script._compat import text_type
from app.models import Viewer



#creating app instance

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)


@manager.shell
def make_shell_contex():
    return dict(app = app, db = db, Viewer=Viewer)

if __name__ =='__main__':
    manager.run()


