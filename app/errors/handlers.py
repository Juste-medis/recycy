# Gestionnaires d'erreurs
from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "message": "Requête invalide"}), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"success": False, "message": "Non autorisé"}), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "message": "Ressource non trouvée"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"success": False, "message": "Erreur interne du serveur"}), 500