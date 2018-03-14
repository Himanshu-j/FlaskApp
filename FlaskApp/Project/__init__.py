from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'databasedb'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/databasedb'
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)


from Project.User.u_views import users_blueprint
from Project.Home.h_views import home_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


from models import User

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
