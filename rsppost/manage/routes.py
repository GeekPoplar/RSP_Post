from flask import render_template,Blueprint,redirect,url_for,flash
from rsppost import db
from rsppost.models import User
from flask_login import login_required,current_user

manage=Blueprint('manage',__name__)


@manage.route('/admin')
@login_required
def admin():
    users = User.query.all ()
    return render_template('admin.html',users=users)


@manage.route('/delete_user/<user_id>')
@login_required
def delete_user(user_id):
    if current_user.is_admin:
        u=User.query.get(user_id)
        db.session.delete(u)
        db.session.commit()
        return redirect(url_for('manage.admin'))
    else:
        flash('你无权进行此操作！')
        return redirect(url_for('manage.admin'))

