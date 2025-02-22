from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger
from flask_jwt_extended import create_access_token
from datetime import timedelta
from app.routes.auth.utils import validate_login, validate_registration

from app import db
from swagger_doc import login_doc, register_doc, logout_doc


class LoginResource(Resource):
    @swagger.operation(**login_doc)
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user, error = validate_login(email, password)
        if error:
            return {"success": False, "message": error}, 400

        user_data = {
            "id": user.id,
            "email": user.email,
            "name": user.username,
        }
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims=user_data,
            expires_delta=timedelta(days=15)
        )
        return {
            "access_token": access_token,
            "success": True,
            "message": "Connexion réussie",
            "user_id": user.id,
        }, 200


class RegisterResource(Resource):
    @swagger.operation(**register_doc)
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user, error = validate_registration(username, email, password)
        if error:
            return {"success": False, "message": error}, 400

        db.session.add(user)
        db.session.commit()

        user_data = {
            "id": user.id,
            "email": user.email,
            "name": user.username,
        }
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims=user_data,
            expires_delta=timedelta(days=15)
        )
        return {
            "access_token": access_token,
            "success": True,
            "message": "Inscription réussie",
            "user_id": user.id,
        }, 201


class LogoutResource(Resource):
    @swagger.operation(**logout_doc)
    def post(self):
        return {"success": True, "message": "Déconnexion réussie"}, 200
