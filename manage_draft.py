import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

if os.path.exists("env.py"):
    import env

app.config = os.environ["SQLALCHEMY_DATABASE_URI"]

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
