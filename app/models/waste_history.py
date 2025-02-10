# Modèle de données pour l'historique des déchets
from app import db
from datetime import datetime

class WasteHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Clé étrangère vers User
    filename = db.Column(db.String(100), nullable=False)  # Nom du fichier image
    prediction = db.Column(db.String(50), nullable=False)  # Catégorie prédite
    confidence = db.Column(db.Float, nullable=False)  # Pourcentage de confiance
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Date et heure de la prédiction