from app import app
from models import db, User, Post, Comment, Reply

with app.app_context():

    users = []
    users.append(User(username="AyLolo", password_hash="apasswordhash"))


    posts = []
    posts.append(Post(user_id=1, title="The First One", content="Flexing My First Post", vote_count=2, comment_count=1))

    comments = []
    comments.append(Comment(post_id=1, user_id=1, content="Flexing My First Comment", vote_count="2"))


    replies = []
    replies.append(Reply(user_id=1, comment_id=1, content="Flexing My First Reply", vote_count=2))

    db.session.add_all(posts)
    db.session.add_all(comments)
    db.session.add_all(replies)
    db.session.commit()

    print("Database Successfully Seeded!")