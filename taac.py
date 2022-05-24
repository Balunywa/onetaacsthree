from taactest import db, Post, Comment

def add_users():
    db.create_all()
    post1 = Post(title='Create First Loop Event', content='Invites for the first loop')
    post2 = Post(title='Create Second Loop Event', content='Invites for the Second loop')
    post3 = Post(title='Create Third Loop Event', content='Invites for the third loop')
    comment1 = Comment(content='Comment for the first post', post=post1)
    comment2 = Comment(content='Comment for the second post', post=post2)
    comment3 = Comment(content='Another comment for the second post', post_id=2)
    comment4 = Comment(content='Another comment for the first post', post_id=1)
    db.session.add_all([post1, post2, post3])
    db.session.add_all([comment1, comment2, comment3, comment4])
    db.session.commit()
    
add_users()

