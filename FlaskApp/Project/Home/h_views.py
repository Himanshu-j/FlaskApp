from flask import render_template, Blueprint
from flask_login import login_required

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


@home_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@home_blueprint.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')
