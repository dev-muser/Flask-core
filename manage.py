import os
from flask_script import Manager, Server
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

manager.add_command('runserver', Server())

@manager.shell
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()
