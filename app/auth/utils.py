# Fonctions utilitaires pour l'authentification
from app.models.user import User
from werkzeug.security import generate_password_hash,check_password_hash 

def validate_login(email, password):
    if not email or not password:
        return None, "Email et mot de passe requis"
    
    user = User.query.filter_by(email=email).first()
 
    if not user or not check_password_hash(user.password, password):
        return None, "Email ou mot de passe incorrect"
    
    return user, None

def validate_registration(username, email, password):
    if not username or not email or not password:
        return None, "Tous les champs sont requis"
    
    if User.query.filter_by(username=username).first():
        return None, "Cet nom d'utilisateur est déjà utilisé"
    
    if User.query.filter_by(email=email).first():
        return None, "Cet email est déjà utilisé"
    
    user = User(username=username, email=email, password= generate_password_hash(password))
    return user, None