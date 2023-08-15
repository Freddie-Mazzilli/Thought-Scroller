from app import app
from models import db, User, Post, Comment, Reply

with app.app_context():

    users = []

    posts = []

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()

    print("Database Successfully Seeded!")