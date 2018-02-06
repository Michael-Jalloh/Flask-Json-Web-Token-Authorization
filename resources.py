from flask_restful import Resource, reqparse
from models import *

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be empty', required=True)
parser.add_argument('password', help='This field cannot be empty', required= True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        if User.get_user(data['username']):
            return {'message':'User {} already exists'.format(data['username'])}
        new_user = User(
            username = data['username'],
            password = data['password']
            )
        try:
            new_user.save()
            return {"message":"username {} was created".format(data['username'])}
        except Exception as e:
            print str(e)
            return {"message":"Something went wrong"}, 500

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = User.get_user(data['username'])
        if not current_user:
            return {'message':'User {} doesn\'t exist'}
        if data['password'] == current_user.password:
            return {"message":"Logged in  as {}".format(current_user.username)}
        else:
            return {"message":"Wrong credentials"}, 404

class UserLogoutAccess(Resource):
    def post(self):
        return {"message":"User logout"}

class UserLogoutRefresh(Resource):
    def post(self):
        return {"message":"User logout"}

class TokenRefresh(Resource):
    def post(self):
        return {"message":"Token refresh"}

class AllUser(Resource):
    def get(self):
        return {"message":"List of users"}

    def post(self):
        return {"message":"Delete All users"}

class SecretResource(Resource):
    def get(self):
        return {"answer": 42 }
