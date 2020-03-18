from flask import render_template,request,Blueprint,url_for,flash,redirect
from flask_login import login_required,current_user
from rsppost.posts.forms import PostForm
from rsppost.models import Post
from rsppost import db

main=Blueprint('main',__name__)

@main.route('/',methods=['GET', 'POST'])
@main.route('/home',methods=['GET', 'POST'])
def home():
    form=PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data,url=form.url.data,body=form.body.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('发布成功，感谢你的贡献！')
        return redirect(url_for('main.home'))
    posts=Post.query.all()
    return render_template('home.html',title='Home',form=form,posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')