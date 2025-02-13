from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import logging

jwt = JWTManager()

db = SQLAlchemy() 

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.config['JWT_SECRET_KEY'] = '*PFiPoWY1vT]v6bL-Ty-?U)[L(}/yF)' 
    
    # Autoriser toutes les origines
    CORS(app)

    db.init_app(app)
    jwt.init_app(app)


    # Configurer le logger
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] - %(message)s'
    ) 
    # # Enregistrement des blueprints
    from app.auth.auth_routes import auth_bp
    from app.main.main_routes import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.add_url_rule("/", endpoint="index")

    #Gestion des erreurs
    from app.errors.handlers import register_error_handlers
    register_error_handlers(app)

    # Création des tables de la base de données
    with app.app_context():
        db.create_all()

    return app
