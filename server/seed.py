from app import app
from models import db, User, Post, Comment, Reply

with app.app_context():

    users = []

    posts = []

    comments = []

    replies = []

    db.session.add_all(posts)
    db.session.add_all(comments)
    db.session.add_all(replies)
    db.session.commit()

    print("Database Successfully Seeded!")