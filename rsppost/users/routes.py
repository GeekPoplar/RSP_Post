from flask import render_template,url_for,flash,redirect,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from rsppost import db
from rsppost.models import User,Post
from rsppost.users.forms import RegistrationForm,LoginForm,Login_with_username_Form

users=Blueprint('users',__name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('users.login'))
    return render_template('register.html',title='注册',form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        #记得判断一下是否存在此用户！
        if not user:
            flash('此邮箱尚未注册，请先注册！')
            return redirect(url_for('users.register'))
        if user.check_password(form.password.data):
            login_user(user,remember=form.remember.data)
            flash('登录成功！')
            return redirect(url_for('main.home'))
        else:
            flash('邮箱或密码错误！')

    return render_template('login.html',title='登录',form=form)


@users.route("/login_with_username", methods=['GET', 'POST'])
def login_with_username():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form=Login_with_username_Form()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        #记得判断一下是否存在此用户！
        if not user:
            flash('此邮箱尚未注册，请先注册！')
            return redirect(url_for('users.register'))
        if user.check_password(form.password.data):
            login_user(user,remember=form.remember.data)
            flash('登录成功！')
            return redirect(url_for('main.home'))
        else:
            flash('用户名或密码错误！')

    return render_template('login_with_username.html',title='登录',form=form)

@users.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('已退出登录')
        return redirect(url_for('main.home'))
    return redirect(url_for('main.home'))

@users.route('/profile/<username>')
@login_required
def profile(username):
    user=User.query.filter_by(username=username).first()
    posts=Post.query.filter_by(author=user).all()
    return render_template('profile.html',title='Profile',posts=posts,user=user)