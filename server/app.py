#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource
from flask_cors import CORS


from models import db, User, Post, Comment, Reply

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scroller.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

bcrypt = Bcrypt(app)

CORS(app)

api = Api(app)

def get_current_user():
    return User.query.where(User.id == session.get("user_id")).first()

def logged_in():
    return bool(get_current_user())

class Users(Resource):

    def get(self):
        users = User.query.all()
        response_body = []
        for user in users:
            relationship = {
                'posts' : user.post.to_dict(),
                'comments': user.comment.to_dict()
            }
            response_body.append(relationship)
        return make_response(jsonify(response_body), 200)
    
# User Signup 

@app.post('/users')
def create_user():
    json = request.json
    pw_hash = bcrypt.generate_password_hash(json['password']).decode('utf-8')
    new_user = User(username=json['username'], password_hash=pw_hash)
    db.session.add(new_user)
    db.session.commit()
    session['user_id'] = new_user.id
    return new_user.to_dict(), 201

# Session Login/Logout

@app.post('/login')
def login():
    json = request.json
    user = User.query.filter(User.username == json["username"]).first()
    if user and bcrypt.check_password_hash(user.password_hash, json["password"]):
        session["user_id"] = user.id
        return user.to_dict(), 201
    
    else:
        return {"error": "Invalid username or password"}, 401
    
@app.get('/current_session')
def check_session():
    if logged_in():
        return get_current_user().to_dict(), 200
    else:
        return {}, 401
    
@app.delete("/logout")
def logout():
    session["user_id"] = None
    return {"message" : "Successfully logged out"}, 204
    
api.add_resource(Users, '/users')

class Posts(Resource):

    def get(self):
        posts = Post.query.all()
        response_body = []
        for post in posts:
            response_body.append(post.to_dict())
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        try:
            data = request.get_json()
            new_post = Post(
                title = data.get('title'),
                content = data.get('content'),
                vote_count = data.get('vote_count'),
                comment_count = data.get('comment_count')
            )
            db.session.add(new_post)
            db.session.commit()
            response_body = new_post.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)

api.add_resource(Posts, '/posts')

class PostsById(Resource):

    def get(self, id):
        post = Post.query.filter(Post.id == id).first()
        if not post:
            response_body = {"error": "Post not found."}
            return make_response(jsonify(response_body), 404)
        response_body = post.to_dict()

        comment_list = []
        for comment in post.comments:
            comment_dict = comment.to_dict()
            comment_list.append(comment_dict)

        return make_response(jsonify(response_body), 200)
    
    def patch(self, id):
        post = Post.query.filter(Post.id == id).first()
        if not post:
            response_body ={"error": "Post not found."}
            return make_response(jsonify(response_body), 404)
        try:
            data = request.get_json()
            for key in data:
                setattr(post, key, data.get(key))
            db.session.commit()
            return make_response(jsonify(post.to_dict()), 202)
        except ValueError:
            response_body = {'errors': ['Validation Errors']}
            return make_response(jsonify(response_body), 400)
        
    def delete(self, id):
        post = Post.query.filter(Post.id == id).first()
        if not post:
            response_body = {'error': 'Post not found.'}
            return make_response(jsonify(response_body), 404)
        db.session.delete(post)
        db.session.commit()
        response_body = {}
        return make_response(jsonify(response_body), 204)
    
api.add_resource(PostsById, '/posts/<int:id>')

class Comments(Resource):

    def get(self):
        comments = Comment.query.all()
        response_body = []
        for comment in comments:
            response_body.append(comment.to_dict())
        return make_response(jsonify(response_body), 200)
    
    def post(self):
        try:
            data = request.get_json()
            new_comment = Comment(
                post_id = data.get('post_id'),
                content = data.get('content'),
                vote_count = data.get('vote_count')
            )
            db.session.add(new_comment)
            db.session.commit()
            response_body = new_comment.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['Validation Errors']}
            return make_response(jsonify(response_body), 400)
        
api.add_resource(Comments, '/comments')
            

        


        