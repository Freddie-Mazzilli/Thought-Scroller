#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource
from flask_cors import CORS
from functools import wraps


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

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

class Users(Resource):

    def get(self):
        users = User.query.all()
        response_body = []
        for user in users:
            relationship = {
                'posts' : [post.to_dict() for post in user.posts],
                'comments':[comment.to_dict() for comment in user.comments],
                'replies': [reply.to_dict() for reply in user.replies]
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

        user_id = session["user_id"]
        user = User.query.filter_by(id=user_id).first()

        if not user:
            return jsonify({'message': 'User not found'}), 404

        try:
            data = request.get_json()
            new_post = Post(
                user_id = user.id,
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

class PostsByUser(Resource):

    def get(self, username):

        user = User.query.filter_by(username = username).first()
        if not user:
            response_body = {"error": "User and their posts not found."}
            return make_response(jsonify(response_body), 404)
        response_body = [post.to_dict() for post in user.posts]

        return make_response(jsonify(response_body), 200)
    
    @login_required
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
    
    @login_required
    def delete(self, id):
        post = Post.query.filter(Post.id == id).first()
        if not post:
            response_body = {'error': 'Post not found.'}
            return make_response(jsonify(response_body), 404)
        db.session.delete(post)
        db.session.commit()
        response_body = {}
        return make_response(jsonify(response_body), 204)
    
api.add_resource(PostsByUser, '/<string:username>/posts/<int:id>')

if __name__ == '__main__':
    app.run(port=7000, debug=True)
        




        





            

        


        