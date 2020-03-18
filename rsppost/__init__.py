from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from rsppost.config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

db=SQLAlchemy()
migrate=Migrate()
login=LoginManager()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    login.login_view='users.login'

    from rsppost.main.routes import main
    from rsppost.users.routes import users
    from rsppost.manage.routes import manage
    from rsppost.posts.routes import posts

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(manage)
    app.register_blueprint(posts)


    return app