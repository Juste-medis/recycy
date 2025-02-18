from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger
 
from app import db
from swagger_doc import login_doc 

class IndexRessource(Resource):
    @swagger.operation(**login_doc)
    def get(self): 
        return {
            "hello":"you are ok" , 
        }, 200
 