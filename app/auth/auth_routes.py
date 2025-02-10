# Importer les bibliothèques nécessaires
from flask import request, jsonify, Blueprint

from app.auth.utils import validate_login, validate_registration
from app.models.user import User
from app import db
from flask_jwt_extended import  create_access_token
from datetime import timedelta


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user, error = validate_login(email, password)
    if error:
        return jsonify({"success": False, "message": error}), 400

    # Crée un token JWT
    user_data = { "id": user.id, "email": user.email, "name": user.username, }
    access_token = create_access_token( identity=str(user.id), additional_claims=user_data, expires_delta=timedelta(days=15) )
    return jsonify({"access_token": access_token,"success": True, "message": "Connexion réussie", "user_id": user.id},), 200
 
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')   
    password = data.get('password')

    user, error = validate_registration(username, email, password)
    if error:
        return jsonify({"success": False, "message": error}), 400

    db.session.add(user)
    db.session.commit()

    user_data = { "id": user.id, "email": user.email, "name": user.username, }
    access_token = create_access_token( identity=str(user.id), additional_claims=user_data, expires_delta=timedelta(days=15) )
    
    return jsonify({"access_token": access_token, "success": True, "message": "Inscription réussie", "user_id": user.id}), 201

@auth_bp.route('/logout', methods=['POST'])
def logout():
    
    return jsonify({"success": True, "message": "Déconnexion réussie"}), 200