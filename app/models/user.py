# Modèle de données pour les utilisateurs
from app import db

def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    waste_history = db.relationship('WasteHistory', backref='user', lazy=True)  # Relation avec l'historique des déchets