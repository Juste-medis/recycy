from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import logging
from flask_restful_swagger import swagger
from flask_restful import Api


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

    api = swagger.docs(Api(app), apiVersion='1.0',  
                    description='Documentation de l\'api vision rec')

    # Configurer le logger
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] - %(message)s'
    ) 
    # # Enregistrement des blueprints

    from app.routes.auth.auth_routes import LoginResource, RegisterResource, LogoutResource
    from app.routes.main.main_routes import SingleUpload, WasteHistoryCall
    from app.routes.main.school_routes import CreateSchool,GetSchoolsResource , GetSchoolResource,UpdateSchoolResource,DeleteSchoolResource
    from app.routes.main.challenge_routes import CreateChallengeResource, GetChallengesResource,GetChallengeResource,UpdateChallengeResource,DeleteChallengeResource

    api.add_resource(LoginResource, '/auth/login')
    api.add_resource(RegisterResource, '/auth/register')
    api.add_resource(LogoutResource, '/auth/logout')

    api.add_resource(SingleUpload, '/waste/classify')
    api.add_resource(WasteHistoryCall, '/waste/history')
 
    api.add_resource(CreateSchool, '/schools/create')
    api.add_resource(GetSchoolsResource, '/schools')
    api.add_resource(GetSchoolResource, '/schools/<int:id>')
    api.add_resource(UpdateSchoolResource, '/schools/<int:id>/update')
    api.add_resource(DeleteSchoolResource, '/schools/<int:id>/delete')

    api.add_resource(CreateChallengeResource, '/challenges/create')
    api.add_resource(GetChallengesResource, '/challenges')
    api.add_resource(GetChallengeResource, '/challenges/<int:id>')
    api.add_resource(UpdateChallengeResource, '/challenges/<int:id>/update')
    api.add_resource(DeleteChallengeResource, '/challenges/<int:id>/delete')

    app.add_url_rule("/", endpoint="index")

    #Gestion des erreurs
    from app.errors.handlers import register_error_handlers
    register_error_handlers(app)

    # Création des tables de la base de données
    with app.app_context():
        db.create_all()

    return app
