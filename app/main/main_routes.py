# Routes principales de l'application
from flask import request, jsonify, Blueprint
from app.main.utils import process_image
from app.models.waste_history import WasteHistory
from app import db
from datetime import datetime
from flask_jwt_extended import  jwt_required, get_jwt_identity

main_bp = Blueprint("vision", __name__,)

@main_bp.route("/")
def index():
    """Show all the posts, most recent first."""
     
    return  """hello"""

@main_bp.route("/hello")
def indexhello():

    return jsonify({"hello": "hello my friend"}), 200



@main_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "Aucun fichier fourni"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "message": "Aucun fichier sélectionné"}), 400
  

    # Traitement de l'image
    predicted_class, confidence = process_image(file)
    current_user = get_jwt_identity()

    # Enregistrement dans l'historique
    waste_history = WasteHistory(
        user_id=current_user,
        filename=file.filename,
        prediction=predicted_class,
        confidence=confidence
    )
    db.session.add(waste_history)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Classification réussie",
        "prediction": predicted_class,
        "treatment": "organic",#or recyclabre
        "confidence": confidence
    }), 200

@main_bp.route('/history', methods=['GET'])
@jwt_required()
def history():
    current_user = get_jwt_identity()
    waste_history = WasteHistory.query.filter_by(user_id=current_user).all()
    history_data = [{
        "id": entry.id,
        "filename": entry.filename,
        "prediction": entry.prediction,
        "confidence": entry.confidence,
        "timestamp": entry.timestamp.isoformat()
    } for entry in waste_history]

    return jsonify({"success": True, "history": history_data}), 200