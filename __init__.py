# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:new-user@localhost/pemeringkatan'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



    db.init_app(app)

#    app.config['MYSQL_HOST'] = 'localhost'
#    app.config['MYSQL_USER'] = 'andi'
#    app.config['MYSQL_PASSWORD'] = 'andi12345'
#    app.config['MYSQL_DB'] = 'quisioner_sdid2'
#    mysql = MySQL(app)

    #login_manager = LoginManager()
    #login_manager.login_view = 'auth.login'
    #login_manager.init_app(app)

    #from .models import Users

    #@login_manager.user_loader
    #def load_user(id_users):
        # since the user_id is just the primary key of our user table, use it in the query for the user
    #    return Users.query.get(int(id_users))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .view import view as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
