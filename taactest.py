import os
import pyodbc
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, 
                     BooleanField, DateTimeField, 
                     RadioField, SelectField, 
                     TextAreaField)

from wtforms.validators import DataRequired
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy


params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=cbserver-one.database.windows.net;DATABASE=onetaacs;UID=balunlu;PWD=Test#123450")

app = Flask(__name__)

app.config['SECRET_KEY'] = 'test'

#app.config['SQLALCHEMY_DATABASE_URL'] = 'sqllite:///'+os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post')

    def __repr__(self):
        return f'<Post "{self.title}">'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return f'<Comment "{self.content[:20]}...">'
    
    
# ...

@app.route('/')
def index():
    posts = Post.query.all()   
    return render_template('index.html', posts=posts)

# ...

@app.route('/<int:post_id>/', methods=('GET', 'POST'))
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        comment = Comment(content=request.form['content'], post=post)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('post', post_id=post.id)) 
    return render_template('post.html', post=post)

# ...

@app.route('/comments/')
def comments():
    comments = Comment.query.order_by(Comment.id.desc()).all()
    return render_template('comments.html', comments=comments)


#if __name__ == '__main__':
#    app.run(debug=True)

