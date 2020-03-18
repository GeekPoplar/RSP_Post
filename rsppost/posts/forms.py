from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title=StringField('标题',validators=[DataRequired()])
    url=StringField('文章链接',validators=[DataRequired()])
    body=TextAreaField('推荐语',validators=[DataRequired()])
    submit=SubmitField('发表')

class CommentForm(FlaskForm):
    content=StringField("评论",validators=[DataRequired()])
    submit=SubmitField('发表')