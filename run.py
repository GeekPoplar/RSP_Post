from rsppost import create_app,db
from rsppost.models import User,Post,Comment

app=create_app()

app.app_context().push()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post,'Comment':Comment}

if __name__=='__main__':
    app.run()