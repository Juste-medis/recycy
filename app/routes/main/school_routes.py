from flask import request, jsonify
from flask_restful import Resource
from flask_restful_swagger import swagger
from app import db
from app.models.school import School
from swagger_doc import create_school_doc, get_schools_doc, get_school_doc, update_school_doc, delete_school_doc

class CreateSchool(Resource):
    @swagger.operation(**create_school_doc)
    def post(self):
        data = request.get_json()
        new_school = School(
            name=data.get('name'),
            contact_email=data.get('contact_email'),
            city=data.get('city')
        )
        db.session.add(new_school)
        db.session.commit()
        return {'message': 'École créée avec succès'} , 201

class GetSchoolsResource(Resource):
    @swagger.operation(**get_schools_doc)
    def get(self):
        schools = School.query.all()
        return [{
            'id': school.id,
            'name': school.name,
            'contact_email': school.contact_email,
            'city': school.city
        } for school in schools], 200

class GetSchoolResource(Resource):
    @swagger.operation(**get_school_doc)
    def get(self, school_id):
        school = School.query.get_or_404(school_id)
        return {
            'id': school.id,
            'name': school.name,
            'contact_email': school.contact_email,
            'city': school.city
        } , 200

class UpdateSchoolResource(Resource):
    @swagger.operation(**update_school_doc)
    def put(self, school_id):
        school = School.query.get_or_404(school_id)
        data = request.get_json()
        school.name = data.get('name', school.name)
        school.contact_email = data.get('contact_email', school.contact_email)
        school.city = data.get('city', school.city)
        db.session.commit()
        return {'message': 'École mise à jour avec succès'} , 200

class DeleteSchoolResource(Resource):
    @swagger.operation(**delete_school_doc)
    def delete(self, school_id):
        school = School.query.get_or_404(school_id)
        db.session.delete(school)
        db.session.commit()
        return {'message': 'École supprimée avec succès'}, 200
