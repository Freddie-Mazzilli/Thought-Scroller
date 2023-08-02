from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    posts = db.relationship("Post", back_populates="user")
    comments = db.relationship("Comment", back_populates="user")
    replies = db.relationship("Reply", back_populates="user")

    # Serializer
    serialize_rules = ('-posts', '-comments', 'replies')

class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"

    # Fields
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    vote_count = db.Column(db.Integer, default=1)
    comment_count = db.Column(db.Integer, default=0)

    # Relationships 

    users = db.relationship("User", back_populates="post", cascade="all, delete-orphan")
    comments = association_proxy("users", "comment", creator=lambda c: User(comment=c))

    # Serializer
    serialize_rules = ("-users",)

class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)

    content = db.Column(db.String, nullable=False)
    vote_count = db.Column(db.Integer, default=1)
    
    # Relationships 
    users = db.relationship("User", back_populates="comment", cascade="all, delete-orphan")
    reply = db.relationship("Reply", back_populates="comments")

    posts = association_proxy("users", "post", creator=lambda p: User(post=p))

class Reply(db.Model, SerializerMixin):
    __tablename__ = "replies"
    
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    comment_id =db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=False)

    content = db.Column(db.String, nullable=False)
    vote_count = db.Column(db.Integer, default=1)

    # Relationships
    users = db.relationship("User", back_populates="replies", cascade="all, delete-orphan") 
    comments = db.relationship("Comment", back_populates="replies", cascade="all, delete-orphan")
    
    




    

