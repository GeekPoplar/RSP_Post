from flask import render_template,url_for,flash,redirect,Blueprint
from flask_login import current_user,login_required
from rsppost import db
from rsppost.posts.forms import PostForm,CommentForm
from rsppost.models import Post,Comment

posts=Blueprint('posts',__name__)



@posts.route('/delete_post/<post_id>')
@login_required
def delete_post(post_id):
    p=Post.query.get(post_id)
    if current_user.is_authenticated and (current_user==p.author or current_user.is_admin):
        db.session.delete(p)
        db.session.commit()
        return redirect(url_for('main.home'))

@posts.route('/like_post/<post_id>')
@login_required
def like_post(post_id):
    p=Post.query.get(post_id)
    
    if current_user.is_authenticated:
        p.likes+=1
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('main.home'))

@posts.route('/comment_post/<post_id>',methods=['GET', 'POST'])
@login_required
def comment_post(post_id):
    
    p=Post.query.get(post_id)

    exec('CommentForm_{}={}'.format(post_id,1))
    locals()['CommentForm'+str(post_id)]=CommentForm()
    if locals()['CommentForm'+str(post_id)].validate_on_submit():
        c=Comment(content=locals()['CommentForm'+str(post_id)].content.data,user_id=current_user.id,post_id=post_id)
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('comment_post.html',title='评论',form=locals()['CommentForm'+str(post_id)])
        
@posts.route('/delete_comment/<comment_id>')
@login_required
def delete_comment(comment_id):
    c=Comment.query.get(comment_id)
    if current_user.is_authenticated and (current_user==c.author or current_user.is_admin or current_user==p.father_post.author):
        db.session.delete(c)
        db.session.commit()
        return redirect(url_for('main.home'))