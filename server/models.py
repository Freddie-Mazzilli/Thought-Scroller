from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(120), nullable=False)
    user_post_count = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    posts = db.relationship("Post", back_populates="user", cascade="all, delete-orphan")
    comments = db.relationship("Comment", back_populates="user", cascade="all, delete-orphan")
    replies = db.relationship("Reply", back_populates="user", cascade="all, delete-orphan")

    # Serializer
    serialize_rules = ('-posts', '-comments', 'replies')

    # Login/Signup Data
    def __repr__(self):
        return f'`<User id="{self.id}" username="{self.username}"`>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }

class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    vote_count = db.Column(db.Integer, default=1)
    comment_count = db.Column(db.Integer, default=0)

    # Relationships 
    user = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")

    # Serializer
    serialize_rules = ("-user", "-comments")

class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    content = db.Column(db.String, nullable=False)
    vote_count = db.Column(db.Integer, default=1)
    
    # Relationships 
    user = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")
    replies = db.relationship("Reply", back_populates="comment")

    # Serializer
    serialize_rules = ("-user", "-post", "-replies")

class Reply(db.Model, SerializerMixin):
    __tablename__ = "replies"
    
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=False)

    content = db.Column(db.String, nullable=False)
    vote_count = db.Column(db.Integer, default=1)

    # Relationships
    user = db.relationship("User", back_populates="replies") 
    comment = db.relationship("Comment", back_populates="replies")

    # Serializer
    serialize_rules = ("-user", "-comment")