# Modèle de données pour les utilisateurs
from app import db
from datetime import datetime

def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    waste_history = db.relationship('WasteHistory', backref='user', lazy=True)  # Relation avec l'historique des déchets
    created_at = db.Column(db.DateTime, default=datetime.now)



# 8. Jetons Utilisateurs (UserToken)
class UserToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    token_type = db.Column(db.String(50))
    token_value = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)


# 9. Paramètres Utilisateurs (UserSetting)
class UserSetting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    notifications_enabled = db.Column(db.Boolean, default=True)
    language = db.Column(db.String(10), default='en')
    created_at = db.Column(db.DateTime, default=datetime.now)



# 5. Notifications (Notification)
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(255))
    read = db.Column(db.Boolean, default=False)
    sent_at = db.Column(db.DateTime, default=datetime.now)
