from .schema import User
from flask import session, request
from datetime import datetime, timedelta
import jwt
from wersut.config import JWTConfig
from pymongo import MongoClient
from foundation.core.api.helper import make_resource_response, make_error

client = MongoClient()
db = client.test_schema
user = db.user


def __setup__(module):
    module.resource('user', User)

    @module.endpoint("/user/login", methods=["POST"])
    def login():
        session.clear()
        request_data = request.json or request.form.to_dict()

        if not request_data.get("username", None):
            return make_error(400, description="[username] is required.")

        if not request_data.get("password", None):
            return make_error(400, description="[password] is required.")

        user_info = user.find_one({"username": request_data.get('username')})
        if user_info is None:
            return make_error(400, description="Username is not exist, please choose another.")

        if not user_info["password"] == request_data.get("password"):
            return make_error(400, description="password is wrong")

        session["username"] = request_data.get("username")

        return "asd"
