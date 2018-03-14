from flask import redirect, render_template, request, url_for, Blueprint
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import LoginForm, RegisterForm
from Project import db
from Project.models import User


users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember.data)
                    return redirect(url_for('home.welcome'))

        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    hashed_password = generate_password_hash(form.password.data, method='sha256')
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        print(user)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.welcome'))
    return render_template('register.html', form=form)
